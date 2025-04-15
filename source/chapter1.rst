===============================
Capitulo 1: Serviços de viatura
===============================

.. _introducao_cap1:

Introdução
================================================================================
A criação automática de serviços de viatura pode ser efectuada utilizando dois métodos diferentes, nomeadamente:

* O modelo básico
* O modelo exacto

The objective function is given by:

.. math:: Z = \sum_{j \in D} c_{j} x_j + \sum_{i \in T} \lambda_i(1 - a_{ij} x_j)
        :label: equation_1

As shown in equation :math:numref:`equation_1`, the objective function...


O transporte rodoviario e logistica de distribuição no contexto da industria automóvel é de extrema relevância.
É através destes processos logisticos que se faz o abastecimento da materia prima necessária para os mais diversos
processos de produção e manutenção de veículos automóveis.

Checking Trip Compatibility
=========================

The ``AreCompatible`` method determines if two trips can be executed sequentially by the same vehicle. It considers various constraints including timing, support time requirements, and depot rest stops.

.. code-block:: csharp

    private bool AreCompatible(int i, int j)
    {
        EMTrip trip_i = _listViableTrips[i];
        EMTrip trip_j = _listViableTrips[j];

        bool areCompatible = false;
        int idleTime;

        if (trip_j.StartTime >= trip_i.EndTime)
        {
            //Case when trip_i endNode is the same as trip_j startNode
            if (trip_i.EndNode.Id == trip_j.StartNode.Id)
            {
                idleTime = trip_j.StartTime - trip_i.EndTime;

                if (idleTime >= trip_i.SupportTime)
                {
                    if (idleTime <= trip_i.MaxStopTime)
                    {
                        int costPenaltyTerminusStopTime = idleTime * _instance.Parameters.PenaltyTerminusStopTime;
                        int costChangeLine = 0;
                        if (trip_i.LineID != trip_j.LineID)
                        {
                            costChangeLine = _instance.Parameters.PenaltyLineChange;            //line change cost
                        }

                        _c_ij[i, j] = costPenaltyTerminusStopTime + costChangeLine;
                        _travelTimeBetweentrips[i, j] = 0;
                        _travelDistanceBetweenTrips[i, j] = 0;

                        return true;
                    }
                    else
                    {
                        if (trip_i.EndNode.Id == _depot.Id)
                        {
                            if (idleTime >= _instance.Parameters.MinStopTimeDepot &&
                                idleTime <= _instance.Parameters.MaxStopTimeDepot)
                            {
                                int costPenaltyDepotStopTime = idleTime * _instance.Parameters.PenaltyDepotStopTime;
                                int costChangeLine = 0;
                                if (trip_i.LineID != trip_j.LineID)
                                {
                                    costChangeLine = _instance.Parameters.PenaltyLineChange;
                                }
                                _c_ij[i, j] = costPenaltyDepotStopTime + costChangeLine;
                                _travelTimeBetweentrips[i, j] = 0;
                                _travelDistanceBetweenTrips[i, j] = 0;

                                return true;
                            }
                        }
                        else
                        {
                            return CheckIfRestAtDepotPossible(i, j);
                        }
                    }
                }
                else
                {
                    if (trip_i.SupportTime - idleTime <= trip_j.MaxDelayTime)
                    {
                        int costTerminusStopTime = trip_i.SupportTime * _instance.Parameters.PenaltyTerminusStopTime;
                        int costDelay = (trip_i.SupportTime - idleTime) * _instance.Parameters.PenaltyDelayTime;
                        int costChangeLine = 0;
                        if (trip_i.LineID != trip_j.LineID)
                        {
                            costChangeLine = _instance.Parameters.PenaltyLineChange;
                        }

                        _c_ij[i, j] = costTerminusStopTime + costDelay + costChangeLine;
                        _travelTimeBetweentrips[i, j] = 0;
                        _travelDistanceBetweenTrips[i, j] = 0;

                        return true;
                    }
                }
            }
            else
            {
                int travelTime = GetBestTravelTime(trip_i.EndNode.Id, trip_j.StartNode.Id,
                                                 trip_i.EndTime, false);

                if (travelTime != int.MaxValue)
                {
                    idleTime = trip_j.StartTime - trip_i.EndTime - travelTime;

                    if (idleTime >= trip_i.SupportTime)
                    {
                        if (idleTime <= trip_j.MaxStopTime)
                        {
                            int costStopTime = idleTime * _instance.Parameters.PenaltyTerminusStopTime;
                            int costPenaltyemptyTripTime = travelTime * _instance.Parameters.PenaltyEmptyTrip;
                            int costChangeLine = 0;
                            if (trip_i.LineID != trip_j.LineID)
                            {
                                costChangeLine = _instance.Parameters.PenaltyLineChange;
                            }
                            _c_ij[i, j] = costStopTime + costPenaltyemptyTripTime + costChangeLine;
                            _travelTimeBetweentrips[i, j] = travelTime;
                            _travelDistanceBetweenTrips[i, j] = _bestLink.TotalDistance;

                            return true;
                        }
                        else
                        {
                            return CheckIfRestAtDepotPossible(i, j);
                        }
                    }
                    else
                    {
                        if (trip_i.SupportTime - idleTime <= trip_j.MaxDelayTime)
                        {
                            int costStopTime = trip_i.SupportTime * _instance.Parameters.PenaltyTerminusStopTime;
                            int costDelay = (trip_i.SupportTime - idleTime) * _instance.Parameters.PenaltyDelayTime;
                            int costPenaltyemptyTripTime = travelTime * _instance.Parameters.PenaltyEmptyTrip;
                            int costChangeLine = 0;
                            if (trip_i.LineID != trip_j.LineID)
                            {
                                costChangeLine = _instance.Parameters.PenaltyLineChange;
                            }
                            _c_ij[i, j] = costStopTime + costPenaltyemptyTripTime + costDelay + costChangeLine;
                            _travelTimeBetweentrips[i, j] = travelTime;
                            _travelDistanceBetweenTrips[i, j] = _bestLink.TotalDistance;

                            return true;
                        }
                    }
                }
                else
                {
                    return CheckIfRestAtDepotPossible(i, j);
                }
            }
        }

        return areCompatible;
    }

Method Description
----------------

This method evaluates whether two trips (``trip_i`` and ``trip_j``) can be executed sequentially by checking various constraints:

1. Temporal Compatibility
   * Trip j must start after trip i ends (``trip_j.StartTime >= trip_i.EndTime``)
   * Considers required support time between trips
   * Handles cases where delay is necessary

2. Spatial Compatibility
   * Handles cases where trips end and start at the same node
   * Evaluates travel time between different nodes
   * Considers depot rest stops when necessary

3. Cost Calculations
   * Terminus stop time penalties
   * Line change penalties
   * Empty trip penalties
   * Delay penalties

Parameters
----------

- ``i``: Index of the first trip in ``_listViableTrips``
- ``j``: Index of the second trip in ``_listViableTrips``

Returns
-------

``bool``: True if the trips are compatible, false otherwise.

Dependencies
-----------

- ``EMTrip``: Trip class containing trip information
- ``CheckIfRestAtDepotPossible``: Helper method for checking depot rest possibilities
- ``GetBestTravelTime``: Helper method for calculating optimal travel times between nodes




Mathematical Model
================

This section describes the mathematical model implementation for the Multi-Commodity Flow Vehicle Scheduling Problem.

Model Overview
------------

The model implements a multi-commodity flow formulation where each commodity represents a different vehicle type. The primary goal is to find optimal vehicle schedules while respecting various operational constraints including vehicle autonomy and trip coverage requirements.

Sets and Indices
--------------

* :math:`K`: Set of vehicle types (network layers)
* :math:`V_k`: Set of nodes in layer k
* :math:`i,j \in V_k`: Nodes in layer k
* :math:`T`: Set of trips to be covered

Network Structure
---------------

Each layer k represents a specific vehicle type and contains:

* :math:`|T|` nodes representing trip start points (0 to |T|-1)
* :math:`|T|` nodes representing trip end points (|T| to 2|T|-1)
* 2 additional nodes representing depot source and sink
* Total nodes per layer: :math:`2|T| + 2`

Decision Variables
---------------

Flow Variables
^^^^^^^^^^^^

* :math:`x_{ijk}`: Flow through arc (i,j) in layer k

  * Binary variables for regular arcs: :math:`x_{ijk} \in \{0,1\}`
  * Integer variables for depot-to-depot arcs: :math:`x_{ijk} \in \{0,\ldots,n_k\}`
  * Where :math:`n_k` is the number of vehicles of type k

Distance Variables
^^^^^^^^^^^^^^^

* :math:`d_{ik}`: Accumulated distance at node i in layer k
* Domain: :math:`d_{ik} \in [0,A_k]`
* Where :math:`A_k` is the autonomy distance of vehicle type k

Objective Function
----------------

Minimize total operational costs:

.. math::
   \min \sum_{k \in K} \sum_{i \in V_k} \sum_{j \in V_k} c_{ijk} x_{ijk}

Where :math:`c_{ijk}` represents the operational cost of arc (i,j) in layer k.

Constraints
---------

Flow Conservation
^^^^^^^^^^^^^^^

For each node in each layer, ensure flow balance:

.. math::
   \sum_{j \in V_k} x_{ijk} - \sum_{j \in V_k} x_{jik} = 0 \quad \forall i \in V_k, k \in K

Trip Coverage
^^^^^^^^^^^

Ensure each trip is served exactly once across all layers:

.. math::
   \sum_{k \in K} x_{i(i+|T|)k} = 1 \quad \forall i \in T

Distance-Based Autonomy
^^^^^^^^^^^^^^^^^^^^

1. Source to Trip Connections:

   .. math::
      d_{source,k} + (d^{depot}_i + d^{trip}_i)x_{source,i,k} \leq d_{i,k} + A_k(1-x_{source,i,k})

   Where:

   * :math:`d^{depot}_i`: Distance from depot to trip i
   * :math:`d^{trip}_i`: Distance of trip i
   * :math:`A_k`: Autonomy distance of vehicle type k

2. Trip to Trip Connections:

   For direct connections:

   .. math::
      d_{i,k} + (d_{ij} + d^{trip}_j)x_{ij,k} \leq d_{j,k} + A_k(1-x_{ij,k})

   For connections via depot:

   .. math::
      d_{j,k} \geq (d^{depot}_j + d^{trip}_j)x_{ij,k}

Additional Considerations
----------------------

Depot Rest Periods
^^^^^^^^^^^^^^^

The model handles connections that require rest at the depot:

* If a connection between trips i and j requires depot rest, the accumulated distance is reset
* Special constraints ensure proper tracking of accumulated distance after depot rest
* Different treatment in distance constraints for direct connections vs. depot rest connections

Vehicle Type Compatibility
^^^^^^^^^^^^^^^^^^^^^^

* Each network layer represents a specific vehicle type
* Compatibility between trips and vehicle types is handled through network layer definition
* Vehicle-specific characteristics (autonomy, capacity) are incorporated in layer-specific constraints

Implementation Notes
-----------------

The model is implemented using Gurobi optimization solver with the following key components:

* Variable declaration using appropriate domains (binary, integer, continuous)
* Constraint matrix construction reflecting network structure
* Separate handling of depot connections and regular trip connections
* Efficient constraint generation for autonomy tracking

Solution Output
-------------

The solution provides:

* Optimal vehicle schedules for each vehicle type
* Trip assignments to specific vehicles
* Accumulated distance tracking at each trip completion
* Total operational cost



















.. _problema_cap1:

Problema
================================================================================


.. _modeloBásico_cap1:

Modelo Básico
================================================================================


.. _modeloExato_cap1:

Modelo Exacto
================================================================================

Para o método exacto podemos definir os seguintes parametros:

Validação das ligações entre nós
--------------------------------

No método *validateGraph* verificamos se conseguimos, dado o numero máximo de percursos estabelecido pelo utilizador,
ter ligaçãio entre os diferentes nos presentes na rede. Note-se que, o que se pretende validar, é se todos os bnos têm
pelo menos um arco a entrar e/ou a sair. Caso estes nós não possuam qualquer arco a entrar ou sair temos um aviso.




.. _quebraServicoViaturas_cap1:
Selecção dos nós deverão ser considerados pontos de rendição na quebra de acordo com a linha
============================================================================================

Ao contrário do que era feito anteriormente, o utilizador tem agora oportunidade de selecionar
quais as linhas em que nós considerados como pontos de rendição deverão ser efectivamente considerados
como tal para permitir a partição dos serviços de viatura de acordo




************************
Vehicle Routing Problem
************************

Mathematical Formulation
=======================

This documentation describes the variable declaration for a multi-layer vehicle routing problem implementation.

Sets and Indices
---------------

.. math::

   \begin{align*}
   K &= \text{Set of network layers} \\
   V_k &= \text{Set of vertices in layer } k \in K \\
   T_k &= \text{Set of trips in layer } k \in K \\
   n_k &= |T_k| \text{ (number of trips in layer } k) \\
   |V_k| &= 2n_k + 2 \text{ (including source and sink depot nodes)}
   \end{align*}

Decision Variables
----------------

The primary decision variables are defined as:

.. math::

   x_{ijk} = \begin{cases}
   \{0,1\} & \text{for regular arcs and trip arcs} \\
   \{0,1,\ldots,m_k\} & \text{for depot return arc}
   \end{cases}

Where:

* :math:`i,j \in V_k`: vertices in layer k
* :math:`k \in K`: network layer
* :math:`m_k`: number of vehicles in layer k

Variable Domains
--------------

The variables are defined under different conditions:

1. **Regular Network Arcs**:

   .. math::

      x_{ijk} \in \{0,1\} \quad \forall (i,j,k) \text{ where } (i,j) \text{ is compatible}

2. **Trip Arcs** (connecting start and end of same trip):

   .. math::

      x_{ijk} \in \{0,1\} \quad \forall i < n_k, j = i + n_k, k \in K

3. **Depot Return Arc** (from sink to source):

   .. math::

      x_{ijk} \in \{0,1,\ldots,m_k\} \quad \text{where } i = |V_k| - 1, j = |V_k| - 2

Implementation Details
====================

Compatibility Matrix
------------------

Variables are only declared when the corresponding arc is feasible according to the compatibility matrix:

.. code-block:: text

   ExtendedCompatibilityMatrix_ij[i,j] = true

Variable Declaration Structure
---------------------------

The variables are implemented as a three-dimensional array :code:`x_ijk[V,V,K]` where:

* First dimension (i): origin vertex
* Second dimension (j): destination vertex
* Third dimension (k): network layer

Code Implementation
------------------

The variable declaration follows this logic:

.. code-block:: csharp

   x_ijk = new GRBVar[V, V, K];
   // For each layer k:
   //   For compatible arcs (i,j):
   //     If trip arc: x_ijk ∈ {0,1}
   //     If depot return arc: x_ijk ∈ {0,...,m_k}
   //     Otherwise: x_ijk ∈ {0,1}

.. note::
   All variables are declared only for compatible arcs as defined in the ExtendedCompatibilityMatrix_ij.

.. note::
   The depot return arc (sink → source) has a special domain to allow for multiple vehicles to return to the depot.



************************
Vehicle Routing Problem
************************

[Previous content remains the same...]

Objective Function
=================

The problem minimizes the total cost across all network layers:

.. math::

   \min \sum_{k \in K} \sum_{i \in V_k} \sum_{j \in V_k} c_{ijk} x_{ijk}

Where:

* :math:`c_{ijk}`: cost of using arc (i,j) in layer k
* :math:`x_{ijk}`: decision variable for using arc (i,j) in layer k
* The sum is only computed over compatible arcs as defined in ExtendedCompatibilityMatrix_ij

Implementation Details
--------------------

The objective function is implemented as a linear expression in Gurobi:

.. code-block:: text

   Minimize ∑(c_ijk * x_ijk) for all compatible arcs (i,j) in each layer k

Cost Matrix
----------

The costs :math:`c_{ijk}` are stored in the ExtendedCosts_ij matrix for each layer, where:

* Costs are only defined for compatible arcs
* Compatibility is determined by ExtendedCompatibilityMatrix_ij[i,j]
* Each layer k may have different cost values

.. note::
   The objective function only includes terms for arcs that are marked as compatible in the ExtendedCompatibilityMatrix_ij.

Code Implementation
-----------------

The objective function is constructed as follows:

.. code-block:: csharp

   GRBLinExpr objectiveFunction = new GRBLinExpr();
   // For each layer k:
   //   For each compatible arc (i,j):
   //     Add term: cost_ijk * x_ijk
   // Minimize the resulting expression


[Previous content remains the same...]

Constraints
==========

The problem includes two main types of constraints: flow conservation constraints and cover constraints.

Flow Conservation Constraints
---------------------------

For each node in each layer, the flow entering must equal the flow leaving:

.. math::

   \sum_{j \in V_k} x_{ijk} - \sum_{j \in V_k} x_{jik} = 0 \quad \forall i \in V_k, \forall k \in K

Where:

* First sum represents flow leaving node i in layer k
* Second sum represents flow entering node i in layer k
* Only compatible arcs (i,j) and (j,i) are considered

Implementation Notes:
^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   For each layer k:
       For each node i:
           ∑(x_ijk) - ∑(x_jik) = 0
           where (i,j) and (j,i) are compatible arcs

Cover Constraints
---------------

Each trip must be covered exactly once across all layers:

.. math::

   \sum_{k \in K} \sum_{i \in T_k} x_{i(i+n_k)k} = 1 \quad \forall t \in T

Where:

* T is the set of all trips
* T_k is the set of trips in layer k
* n_k is the number of trips in layer k
* x_{i(i+n_k)k} represents the arc connecting the start and end nodes of trip i in layer k

.. note::
   The cover constraint ensures that each trip is assigned exactly once, regardless of which layer it appears in.

Implementation Details
--------------------

The constraints are implemented in two main blocks:

1. **Flow Conservation**:

   .. code-block:: csharp

      // For each layer k:
      //   For each node i:
      //     ∑(outgoing arcs) - ∑(incoming arcs) = 0
      //     where arcs are defined by ExtendedCompatibilityMatrix_ij

2. **Cover Constraints**:

   .. code-block:: csharp

      // For each trip t:
      //   ∑(trip execution variables across all layers) = 1
      //   where trip execution is represented by arc (i, i+n_k)

Mathematical Notation
-------------------

Additional notation used in constraints:

.. math::

   \begin{align*}
   &\text{Sets:} \\
   &T = \text{Set of all trips} \\
   &T_k = \text{Set of trips in layer } k \\
   &\text{Indices:} \\
   &i,j \in V_k \text{ (nodes in layer k)} \\
   &k \in K \text{ (layers)} \\
   &t \in T \text{ (trips)}
   \end{align*}

.. note::
   All constraints are subject to the compatibility matrix ExtendedCompatibilityMatrix_ij, which defines feasible arcs in each layer.


Vehicle Energy Constraints Extension
=================================

Additional Parameters
------------------

.. math::

   \begin{align*}
   E_{max} &= \text{Maximum energy capacity of vehicles} \\
   E_{min} &= \text{Minimum energy threshold required at sink node} \\
   e_t &= \text{Energy consumption of trip } t \\
   e_{ij} &= \text{Energy consumption for deadhead trip between nodes } i \text{ and } j
   \end{align*}

New Decision Variables
-------------------

.. math::

   E_{ik} = \text{Remaining energy level at node } i \text{ in layer } k

Energy Flow Constraints
--------------------

1. **Initial Energy Constraint** (at source node):

   .. math::

      E_{sk} = E_{max} \quad \forall k \in K

   where s is the source node in layer k

2. **Energy Conservation Constraints**:

   .. math::

      E_{jk} \leq E_{ik} - (e_t + e_{ij})x_{ijk} + M(1-x_{ijk}) \quad \forall (i,j) \in A_k, \forall k \in K

   where:
   * M is a large constant
   * e_t is the energy consumption of the trip (if i is a trip node)
   * e_{ij} is the energy consumption of deadhead movement from i to j

3. **Final Energy Threshold** (at sink node):

   .. math::

      E_{tk} \geq E_{min} \quad \forall k \in K

   where t is the sink node in layer k

Implementation Notes
------------------

The model needs to be modified as follows:

1. **Variable Declaration**:

   .. code-block:: csharp

   // Add energy state variables
   E_ik = new GRBVar[V, K];
   for (int k = 0; k < K; k++)
   {
       for (int i = 0; i < V_k; i++)
       {
           E_ik[i,k] = model.AddVar(0.0, E_max, 0.0, GRB.CONTINUOUS,
                                  "E_" + i + "_" + k);
       }
   }

2. **Constraint Addition**:

   .. code-block:: csharp

   // Initial energy at source node
   for (int k = 0; k < K; k++)
   {
       model.AddConstr(E_ik[sourceNode, k] == E_max,
                      "Initial_Energy_Layer_" + k);
   }

   // Energy conservation
   for (int k = 0; k < K; k++)
   {
       for (int i = 0; i < V_k; i++)
       {
           for (int j = 0; j < V_k; j++)
           {
               if (ExtendedCompatibilityMatrix_ij[i,j])
               {
                   double energyConsumption = GetEnergyConsumption(i, j);
                   model.AddConstr(
                       E_ik[j,k] <= E_ik[i,k] - energyConsumption * x_ijk[i,j,k]
                                   + M * (1 - x_ijk[i,j,k]),
                       "Energy_Conservation_" + i + "_" + j + "_" + k);
               }
           }
       }
   }

   // Final energy threshold
   for (int k = 0; k < K; k++)
   {
       model.AddConstr(E_ik[sinkNode, k] >= E_min,
                      "Final_Energy_Layer_" + k);
   }

Helper Functions
--------------

.. code-block:: csharp

   private double GetEnergyConsumption(int i, int j)
   {
       // If i is a trip node, include trip energy consumption
       double tripEnergy = (i < numberTrips) ? trips[i].EnergyConsumption : 0;
       // Add deadhead movement energy consumption
       double deadheadEnergy = GetDeadheadEnergy(i, j);
       return tripEnergy + deadheadEnergy;
   }



Charging Station Extension
========================

Sets and Parameters
------------------

.. math::

   \begin{align*}
   &\text{New Sets:} \\
   &C = \text{Set of charging stations} \\
   &C_k \subseteq V_k = \text{Set of charging station nodes in layer } k \\
   \\
   &\text{New Parameters:} \\
   &r_c = \text{Charging rate at station } c \text{ (energy units per time unit)} \\
   &t_c = \text{Minimum charging time at station } c \\
   &T_c = \text{Maximum charging time at station } c \\
   &f_c = \text{Fixed cost for using charging station } c \\
   &p_c = \text{Cost per energy unit at station } c
   \end{align*}

Decision Variables
----------------

.. math::

   \begin{align*}
   &\text{Charging Variables:} \\
   &y_{ck} = \begin{cases}
   1 & \text{if charging station } c \text{ is used in layer } k \\
   0 & \text{otherwise}
   \end{cases} \\
   &\tau_{ck} \geq 0 = \text{charging time at station } c \text{ in layer } k \\
   &\chi_{ck} \geq 0 = \text{amount of energy charged at station } c \text{ in layer } k
   \end{align*}

Extended Objective Function
-------------------------

Add charging costs to the original objective:

.. math::

   \min \left(\sum_{k \in K} \sum_{i \in V_k} \sum_{j \in V_k} c_{ijk} x_{ijk} + \sum_{k \in K} \sum_{c \in C_k} (f_c y_{ck} + p_c \chi_{ck})\right)

Additional Constraints
--------------------

1. **Charging Station Energy Balance**:

   .. math::

      E_{jk} = E_{ik} + \chi_{ck} - e_{ij}x_{ijk} \quad \forall c \in C_k, i \in c, j \in V_k, k \in K

2. **Charging Time Limits**:

   .. math::

      t_c y_{ck} \leq \tau_{ck} \leq T_c y_{ck} \quad \forall c \in C_k, k \in K

3. **Energy Charged Relation**:

   .. math::

      \chi_{ck} = r_c \tau_{ck} \quad \forall c \in C_k, k \in K

4. **Maximum Charge Limit**:

   .. math::

      E_{ik} + \chi_{ck} \leq E_{max} \quad \forall c \in C_k, i \in c, k \in K

Implementation Notes
------------------

The model needs to be modified as follows:

.. code-block:: csharp

   // Declare new variables
   y_ck = new GRBVar[C, K];
   tau_ck = new GRBVar[C, K];
   chi_ck = new GRBVar[C, K];

   // Initialize variables
   for (int k = 0; k < K; k++)
   {
       foreach (var c in chargingStations)
       {
           y_ck[c,k] = model.AddVar(0.0, 1.0, 0.0, GRB.BINARY,
                                   "y_" + c + "_" + k);
           tau_ck[c,k] = model.AddVar(0.0, T_c, 0.0, GRB.CONTINUOUS,
                                     "tau_" + c + "_" + k);
           chi_ck[c,k] = model.AddVar(0.0, E_max, 0.0, GRB.CONTINUOUS,
                                     "chi_" + c + "_" + k);
       }
   }


Charging Station Capacity Extension
================================

Additional Parameters
------------------

.. math::

   \begin{align*}
   &Q_c = \text{Capacity (number of charging spots) at station } c \\
   \end{align*}

Capacity Constraints
------------------

For each charging station c and layer k, we need to ensure that the number of vehicles simultaneously charging doesn't exceed the station's capacity. Given our current formulation, we can express this as:

.. math::

   \sum_{i \in V_k} \sum_{j \in V_k} x_{ijk} \leq Q_c \quad \forall c \in C_k, k \in K

   \text{where } i \text{ is a charging station node}

Implementation Notes
------------------

.. code-block:: csharp

   // Add capacity constraints for each charging station
   foreach (var c in chargingStations)
   {
       for (int k = 0; k < K; k++)
       {
           GRBLinExpr stationUsage = new GRBLinExpr();

           // Sum all vehicles using the charging station
           for (int i = 0; i < V_k; i++)
           {
               for (int j = 0; j < V_k; j++)
               {
                   if (IsChargingStationNode(i, c) &&
                       ExtendedCompatibilityMatrix_ij[i,j])
                   {
                       stationUsage.AddTerm(1.0, x_ijk[i,j,k]);
                   }
               }
           }

           model.AddConstr(stationUsage <= Q_c,
                          "Charging_Capacity_" + c + "_" + k);
       }
   }


[Previous content remains the same until Time Flow Constraints section]

Time Flow Constraints
------------------

1. **Time Propagation** (for non-charging nodes):

   .. math::

      T_{jk} \geq T_{ik} + (tt_{ij} + st_i)x_{ijk} - M(1-x_{ijk}) \quad \forall i,j \in V_k \setminus C_k, k \in K

2. **Time Propagation with Charging** (Linearized):

   .. math::

      \begin{align*}
      &T_{jk} \geq T_{ik} + tt_{ij}x_{ijk} + \tau_{ck} - M(1-x_{ijk}) \quad \forall i \in C_k, j \in V_k, k \in K \\
      &\tau_{ck} \leq My_{ck} \quad \forall c \in C_k, k \in K \\
      &\tau_{ck} \geq \tau_{min}y_{ck} \quad \forall c \in C_k, k \in K \\
      &\tau_{ck} \leq \tau_{max}y_{ck} \quad \forall c \in C_k, k \in K
      \end{align*}

Where:
* y_{ck} is the binary variable indicating if station c is used in layer k
* τ_{ck} is now directly constrained by the y_{ck} variable
* The charging time is added separately from the travel time

Implementation Notes
------------------

.. code-block:: csharp

   // Time flow constraints with charging
   for (int k = 0; k < K; k++)
   {
       for (int i = 0; i < V_k; i++)
       {
           if (IsChargingStation(i))
           {
               int c = GetStationIndex(i);
               for (int j = 0; j < V_k; j++)
               {
                   if (ExtendedCompatibilityMatrix_ij[i,j])
                   {
                       // Linear time flow with charging
                       model.AddConstr(
                           T_ik[j,k] >= T_ik[i,k] +
                           tt_ij[i,j] * x_ijk[i,j,k] +
                           tau_ck[c,k] -
                           M * (1 - x_ijk[i,j,k]),
                           "Time_Flow_Charging_" + i + "_" + j + "_" + k);
                   }
               }

               // Charging time constraints
               model.AddConstr(tau_ck[c,k] <= M * y_ck[c,k],
                             "Charging_Time_Upper_" + c + "_" + k);
               model.AddConstr(tau_ck[c,k] >= tau_min * y_ck[c,k],
                             "Charging_Time_Lower_" + c + "_" + k);
               model.AddConstr(tau_ck[c,k] <= tau_max * y_ck[c,k],
                             "Charging_Time_Max_" + c + "_" + k);
           }
       }
   }

Final model
------------

.. _ev_scheduling_model:

Vehicle Scheduling Model
========================

Mathematical Formulation
-------------------------

Let:

- :math:`x_{i,j,k}` be a binary decision variable indicating whether an electric vehicle travels from node :math:`i` to node :math:`j` in layer :math:`k`.
- :math:`t_i` be the time at node :math:`i`.
- :math:`e_i` be the energy level at node :math:`i`.
- :math:`\text{charge}_i` be the charging amount at node :math:`i`.
- :math:`\text{timeCharge}_i` be the charging time at node :math:`i`.

Objective Function
^^^^^^^^^^^^^^^^^^

.. math::
   \min \sum_{(i,j,k)} c_{i,j,k} x_{i,j,k} + \sum_i 100 \cdot \text{charge}_i

Constraints
^^^^^^^^^^^

1. **Flow Conservation:**

   .. math::
      \sum_{j} x_{i,j,k} - \sum_{j} x_{j,i,k} = 0, \quad \forall i, k

2. **Trip Coverage:**

   .. math::
      x_{0,2,0} = 1, \quad x_{1,3,0} = 1

3. **Time Constraints:**

   .. math::
      t_{j} \geq t_{i} + d_{i,j} - M(1 - x_{i,j,k}), \quad \forall (i,j,k)

4. **Energy Conservation:**

   .. math::
      e_j \geq e_i - \lambda x_{i,j,k} + \text{charge}_i, \quad \forall (i,j,k)

5. **Battery Limits:**

   .. math::
      e_i + \text{charge}_i \leq 100, \quad \forall i

6. **Charging Constraints:**

   .. math::
      \text{charge}_i = 6.66 \cdot \text{timeCharge}_i, \quad \forall i

7. **Binary and General Constraints:**

   .. math::
      x_{i,j,k} \in \{0,1\}, \quad x_{9,8,0} \leq 31