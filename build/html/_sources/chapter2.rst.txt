==================================
Capítulo 2: Serviços de tripulante
==================================

.. _introducao_cap2:

Introdução
================================================================================

O modulo de planeamento automático dos serviços de tripulantes pode ser acedido na barra como indicado na figura
(see Figure :ref:`ui_tripulantes_front`)

O UI de planeamento de tripulantes é composto por dois separadores: 1) *Principal*, e 2) *Opções adicionais*

Separador *Principal*
=====================

O separador *Principal* é composto por 6 grandes grupos:

* Parâmetros do modelo
* Selecção tipos de serviço de tripulante
* Geração de serviços
* Execução do modelo
* Geração de serviços
* Solução tipos de serviço de tripulante
* Informação da solução

.. figure:: _static/figures/UI_tripulantes_front.png
   :scale: 30%
   :align: center
   :name: ui_tripulantes_front

   Crew schedule planning UI - *Principal* tab.

Parâmetros do modelo
_____________________

Tipos de modelo
...............

.. index:: UIcrew:tipos_modelo
.. index:: UIcrew:tipos_modelo

O utilizador pode escolher entre dois tipos de modelo:

* **Modelo de partição.** Não permite sobrecobertura. Cada *bloco de trabalho* tem de ser coberto obrigatoriamente por apenas um serviço de tripulante.
* **Modelo de cobertura.** Permite sobrecobertura. Cada *bloco de trabalho* tem de ser coberto por pelo menos um serviço de tripulante, mas poderá ser por mais.

.. attention::
   * Podem existir *blocos de trabalho* que não são cobertos por qualquer serviço de tripulante dado pelo gerador. Os *blocos de trabalho* que não são cobertos por qualquer serviço de tripulante não são tidos em conta no modelo.
   * No caso dos problemas de partição, e de forma a garantir que existe sempre solução para o problema, criam-se tantos *serviços proxy* auxiliares quanto o número de *blocos de trabalho*. Cada um destes serviços apenas cobre um *bloco de trabalho* e tem um custo de selecção muito elevado a fim de apenas ser seleccionado em último caso. Desta forma garante-se a viabilidade do problema, com a contrapartida de ficarmos com um modelo maior e com implicações ao nível da função objectivo.
   * Dos dois pontos acima resulta que a solução do problema pode ter blocos de trabalho não cobertos.

Tipos de objectivo
..................

.. index:: UIcrew:tipos_objectivo
.. index:: UIcrew:tipos_objectivo

O utilizador pode escolher 1 de entre 4 objectivos, 2 únicos e 2 multi-objectivo.

* **Objectivos únicos.**
   * minimizar o custo (computacional).
   * minimizar o número de serviços utilizados.

* **Multi-objectivo.**
   * minimizar primeiro o custo e depois o número de serviços.
   * minimizar primeiro o número de serviços e depois o custo.

.. note::
   No que toca às opções multi-objectivo, utilizamos uma abordagem hierárquica, onde se começa por minimizar o objectivo primário, e depois, utilizando a solução do modelo anterior como restrição, optimiza-se o objectivo secundário.

.. figure:: /_static/figures/UICrew_parametros_modelo.png
   :scale: 30%
   :align: center
   :name: UICrew_parametros_modelo

   Parâmetros do modelo.



Separador *Opções adicionais*
=============================

.. figure:: _static/figures/UICrew_aditionalTab.png
   :scale: 30%
   :align: center
   :name: UICrew_aditionalTab

   Crew schedule planning UI - *Opções adicionais* tab.

Deslocação de tripulantes
-------------------------


Outros
------


Adicionar blocos de trabalho
----------------------------

Blocos de preparação
____________________

O utilizador pode optar por incluir blocos de preparação no inicio do serviço, no fim e/ou blocos de praparação intermédios


.. _problema_cap2:

Problema: Crew scheduling problem
=================================


The crew scheduling problem consists in optimally assigning crews to the vehicles, assuming that vehicle blocks are
known and that the operational/contractual/union rules are satisfied :cite:`mesquitasolving`



.. _modeloExato_cap2:

Exact model
================================================================================

The solution method encompasses two phases: 1) duties generation; and 2) an exact partitioning model.

In the first phase, we generate the complete set of feasible duties

.. _dutyGeneratorEngine_cap2:

Duty Generator Engine
=====================

The duties generator comprises two main phases:

* Construct the sucessor dictionary for each of the workblocks contining the list of all workblocks that may be considered to be a possible sucessor
* Given the previous sucessor dictionary build all possible duty schedules, starting for every work block

The starting point of the method is the following




.. code-block:: csharp

    foreach (HtxTipoServ tipSer in horario.TServs.Values)
    {
        //Update driver duties parameters if any of the additional preparation work blocks is >0

        //Create the dictionary with every workblock list of sucessor
        buildNewHashSucessor(dur, tipSer, horario.Viagens);

        //Main function encompassing the dynamic programing method for the incremental creation of the driver duties
        geradorEtapa(tipSer, __globalParameters);
    }

.. code-block:: csharp

        private int geradorEtapa(HtxTipoServ tipoServico, GlobalParameters globalParameters)
        {
            int countTramo = 0;
            int percentagem = 0;
            double percentagemAtual;
            int NumTramo = __HashTramo.Count;
            foreach (Pecas tramo in __HashTramo.Values)
            {
                percentagemAtual = countTramo * 100 / NumTramo;
                CaminhoEtapa caminho = new CaminhoEtapa(tipoServico, globalParameters);
                caminho.AddDeleteGeneratedService += Caminho_AddDeleteGeneratedService;

                bool inicioCaminhoValido = caminho.AddPeca(tramo, __ListEstacao);
                if (inicioCaminhoValido)
                {
                    BuildPathService(caminho);
                }
                if (percentagem < (int)percentagemAtual)
                {
                    percentagem = (int)percentagemAtual;
                    UpdateDelegateGerador(8, percentagem, tipoServico.Nome);
                }
                countTramo++;
            }
            return 0;
        }


.. _buildNewHashExplanation:

Explanation of buildNewHashSucessor
-----------------------------------

The `buildNewHashSucessor` function is responsible for...





.. code-block:: pseudocode

   FOR tipoServiço IN TiposServiço DO
       IF prepStart > 0 OR prepEnd > 0 OR prepInterm > 0 THEN
           UpdateDutyTypeParameters(tipoServiço)
       ENDIF
   ENDFOR


Mathematical formulation
========================

The crew scheduling problem can be formulated in several ways (see literature review). The underlying model is simply a set covering/partitioning
model. The aim is to cover the work blocks defined in the vehicle schedule, with the available feasible duties
created with the :ref:`dutyGeneratorEngine_cap2`, so that the objective function is minimised.

The *Crew Scheduling Problem (CSP)* can be formulated as a set covering problem with additional constraints.
Let :math:`W` represent the set of work blocks defined in the vehicle schedule, and :math:`D` the set of feasible duties
generated using the :ref:`dutyGeneratorEngine_cap2`, with :math:`c_d` representing the cost of using the duty in the solution. Additionally, :math:`D_w` represents subsets of duties :math:`d \in D`
that cover work block :math:`w \in W`.

We use binary variables as defined below.

.. math::
    x_i = \text{1 if the generated duty } d \in D \text{, 0 otherwise.}

.. note::
   Besides the decision variable :math:`x_i`, we also consider 4 additional variables representing the number of services below
the minimum or maximum number or proportion as given by the user (incluir referencia ao UI onde isso se mostra)


Given the aforementioned notation the *SCP* can be formulated as follows:

.. math::
    &\mbox{ minimize }     & Z = c_d x_d    &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{d \in D_w} x_d = 1  &  \quad \forall  w \in W     \\
    &                       & \quad x_d \in \{0,1\}             &  \quad \forall  d \in D



The objective function aims to minimise the total cost of the selected duties. The user can select alternative objective
functions. See Alternative objective functions.

The first set of constraints are covering constraints asserting that each task must be covered by at least
one duty. If the inequality becomes an equality, we are stating that a task must
be covered by exactly one duty, and in this case we are in the presence of a set partitioning
problem instead of a set covering problem. As this is a much more restrictive constraint, it is more probable to result
in infeasible models. This issue is managed using the method presented in *Proxy duties*.

The last set of constraints establish the domain of the decision variables.



As shown in equation :math:numref:`equation_1`, the objective function...


.. code-block:: C#

        private void SetEnvironmentAndModel()
        {
            _environment = new GRBEnv(true);
            _environment.Set(GRB.IntParam.OutputFlag, 1);
            _environment.Set(GRB.IntParam.LogToConsole, 1);
            _environment.Set("LogFile", _solverLogFileName);
            _environment.Start();

            _gurobiUsed = true;

            //Set solver and model parameters (If commented the default values will be used)
            SetSolverParameters();

            // Create empty model
            _model = new GRBModel(_environment);
            _model.Set(GRB.StringAttr.ModelName, "GUROBI_SetCoveringModel");
        }




.. _UICrew:

UI - Planeamento serviços de tripulante
================================================================================

No separador principal o utilizador pode definir diversos parâmetros do problema/modelo a resolver, nomeadamente.

* tipos de modelo (cobertura ou partição)
* tipos de objectivo (singular ou multi-objectivo)
* restrições adicionais para limites mínimos e máximos de número e/ou percentagem desejada para cada tipologia de serviço na solução final
* restrições quanto à média das horas trabalhadas (média por tipologia de serviço ou por horário)
* uso da oferta (viagens em cheio e vazias) para a deslocação dos tripulantes (as *boleias*)
* validação da deslocação no final de um serviço
* não obrigar a cobertura de blocos sem viagens de duração superior a determinado valor


Tipos de modelo
---------------------------------------------
.. index:: UIcrew:tipos_modelo
.. index:: UIcrew:tipos_modelo

O utilizador pode escolher entre dois tipos de modelo:

* **Modelo de partição.** Não permite sobrecobertura. Cada *bloco de trabalho* tem de ser coberto obrigatoriamente por apenas um serviço de tripulante.
* **Modelo de cobertura.** Permite sobrecobertura. Cada *bloco de trabalho* tem de ser coberto por pelo menos um serviço de tripulante, mas poderá ser por mais.

.. attention::
   * Podem existir *blocos de trabalho* que não são cobertos por qualquer serviço de tripulante dado pelo gerador. Os *blocos de trabalho* que não são cobertos por qualquer serviço de tripulante não são tidos em conta no modelo.
   * No caso dos problemas de partição, e de forma a garantir que existe sempre solução para o problema, criam-se tantos *serviços proxy* auxiliares quanto o número de *blocos de trabalho*. Cada um destes serviços apenas cobre um *bloco de trabalho* e tem um custo de selecção muito elevado a fim de apenas ser seleccionado em último caso. Desta forma garante-se a viabilidade do problema, com a contrapartida de ficarmos com um modelo maior e com implicações ao nível da função objectivo.
   * Dos dois pontos acima resulta que a solução do problema pode ter blocos de trabalho não cobertos.

Tipos de objectivo
---------------------------------------------
.. index:: UIcrew:tipos_objectivo
.. index:: UIcrew:tipos_objectivo

O utilizador pode escolher um de entre 4 objectivos, 2 únicos e 2 multi-objectivo.

* **Objectivos únicos.**
   * minimizar o custo (computacional).
   * minimizar o número de serviços utilizados.

* **Multi-objectivo.**
   * minimizar primeiro o custo e depois o número de serviços.
   * minimizar primeiro o número de serviços e depois o custo.

.. note::
   No que toca às opções multi-objectivo, utilizamos uma abordagem hierárquica, onde se começa por minimizar o objectivo primário, e depois, utilizando a solução do modelo anterior como restrição, optimiza-se o objectivo secundário.

.. figure:: /_static/figures/UICrew_parametros_modelo.png
   :scale: 30%
   :align: center
   :name: UICrew_parametros_modelo

   Parâmetros do modelo.


Tipos de serviços e limites
---------------------------------------------
.. index:: UIcrew:limitesTipologias
.. index:: UIcrew:limitesTipologias

O utilizador pode selecionar as tipologias de serviço de tripulante que quer considerar no modelo (Figura :ref:`UICrew_selecaoTiposServico`).
As tipologias disponiveis são aquelas definidas para o horário, e o :ref:`dutyGeneratorEngine_cap2` apenas irá criar serviços das tipologias activas.

.. figure:: /_static/figures/UICrew_selecaoTiposServico.png
   :scale: 30%
   :align: center
   :name: UICrew_selecaoTiposServico

   Tipos de serviço de tripulante e os seus limites.


Para cada tipologia selecionada é possivel definir valores mínimos e máximos "desejados" para o número de serviços e/ou percentagem
do número de serviços na solução final. Os limites em termos de número e percentagem podem ser utilizados
simultaneamente, e a solução será condicionada pela regra mais restrita.

Estas restrições são ditas "soft", na medida em que podem não ser respeitadas. A diferença entre o efectivo e desejado (*Delta*) é tido em conta no modelo e penalizado na função objectivo.
De momento e para qualquer dos desvios considera-se um custo pre-definido no código  = 1000000.

O calculo do *Delta*, para apresentação no UI, apenas se faz caso o valor seja inferior ao minimo, ou superior ao máximo
estipulado, dado que são as únicas diferenças que são relevantes.

Inserir referência para a parte em que se explica o modelo e a sua implementação.



Média de horas trabalhadas
---------------------------------------------
.. index:: UIcrew:mediasHorasTrabalhadas
.. index:: UIcrew:mediasHorasTrabalhadas

O utilizador pode escolher entre dois tipos, mutuamente exclusivos, de restrições quanto à média de horas trabalhadas:

* por tipologia de serviço de tripulante.
* definindo uma média máxima de horas de trabalho para todo o horário.


.. figure:: /_static/figures/UICrew_mediaTrabalho.png
   :scale: 30%
   :align: center
   :name: UICrew_mediaTrabalho

   Restrições à média de horas de trabalho


.. rubric::  Médias por tipologia de serviço de tripulante

Define que a média de horas trabalhadas por tipologia não ultrapassa a média definida nos respectivos parâmetros (ver figura :ref:`UICrew_paramsTipologias`).
O parãmetro *Tempo de média* representa o valor máximo para a média de horas trabalhadas. Já o parâmetro *Tempo para a média* é um valor adicional que pode ser somado ao tempo de trabalho de cada serviço para o cálculo da média. Por exemplo, serviços do tipo *Seguido* por vezes precisam de um *Tempo para a média* de 30 minutos, quando se usa a restrição da média do horário a 7:30 na Carris.

.. figure:: /_static/figures/UICrew_paramsTipologias.png
   :scale: 30%
   :align: center
   :name: UICrew_paramsTipologias

   Parâmetros da tipologia de serviço


.. rubric::  Média do horário

Define o valor máximo para a média de horas trabalhadas num horário. As tipologias que são *Bocado* (como atributo) não contam para o cálculo da média.



.. _usarOferta:

Uso da oferta (*boleias*)
---------------------------------------------
.. index:: UIcrew:usarOferta
.. index:: UIcrew:usarOferta

A opção *Usar oferta (viagens)*, permite considerar as viagens (em cheio e vazio), ou parte destas,
para as deslocações dos tripulantes, para além do usual conjunto de deslocações de tripulante definidas *a priori* pelo
utilizador. Esta opção pode ser tida em conta juntamente com a :ref:`validacaoDesloc`.
Ao selecionar esta opção, podemos ainda estipular:

* tempo para compensação de atrasos da viagem anterior (tempo depois)
* tempo de antecipação antes da próxima viagem (tempo antes)

Estes tempos permitem estabelecer folgas temporais que permitam acomodar eventuais atrasos.

.. figure:: /_static/figures/UICrew_usarOferta.png
   :scale: 30%
   :align: center
   :name: UICrew_usarOferta

   Usar as viagens para deslocações de tripulantes

.. note::
   O método começa por tentar identificar no conjunto das viagens (em cheio e vazias), uma possivel oportunidade de
   deslocação entre dois pontos verificando o local e hora dos *passing times* das viagens. Caso exista, ficamos com a primeira a ser encontrada. Dado que podemos ter
   muitas alternativas, decidiu-se manter a primeira encontrada ao invés de calcular o mínimo das
   *boleias*. Depois de verificar a existência de *boleias* verificamos a existência de deslocações na lista definida *a priori*
   pelo utilizador. Por fim, comparamos a *boleia* e a *deslocação* e mantemos a alternativa com menor tempo de deslocação.



.. _validacaoDesloc:

Validação da deslocação no final de um serviço
---------------------------------------------
.. index:: UIcrew:validacaoDesloc
.. index:: UIcrew:validacaoDesloc

Ao considerar a opção *Validar deslocação* forçamos a que apenas existam serviços de tripulante que comecem e acabem no
mesmo local ou, no caso de acabarem num local diferente do local inicial, se existir uma ligação
(crew walking times) entre a localização final e a localização inicial que permita chegar ao nó inicial dentro do tempo
máximo de trabalho (inclui tempo extra).

Se para além disso, for selecionada a opção :ref:`usarOferta`, verificar-se-á ainda se existe ligação entre o nó final e
inicial através de uma boleia numa das viagens da "oferta".



.. figure:: /_static/figures/UICrew_validarDeslocacoes.png
   :scale: 30%
   :align: center
   :name: UICrew_validarDeslocacoes

   Validação das deslocações



.. _semVigens:

Não cobertura de blocos sem viagens
-----------------------------------
.. index:: UIcrew:NaoBlocosSemViagens
.. index:: UIcrew:NaoBlocosSemViagens

Esta opção permite ao modelo não ter a obrigação de cobrir blocos de trabalho que não tenham viagens e cuja duração
seja superior ao valor definido pelo utilizador. Estes blocos podem ser cobertos se tal for vantajoso para a resolução do problema.


.. figure:: /_static/figures/UICrew_semViagens.png
   :scale: 30%
   :align: center
   :name: UICrew_semViagens

   Tempo dos blocos sem viagens




.. _infoOutput:

Informação sobre o resultado
----------------------------
.. index:: UIcrew:infoOutput
.. index:: UIcrew:infoOutput


A informação acerca da solução é apresentada em duas grandes areas (ver figura :ref:`UICrew_informacaoSolucao`):

   * Indicadores gerais da solução
   * Indicadores por tipologia de serviço tripulante

.. figure:: /_static/figures/UICrew_informacaoSolucao.png
   :scale: 30%
   :align: center
   :name: UICrew_informacaoSolucao

   Indicadores gerais da solução

.. rubric:: 1) Indicadores gerais da solução

Existem diversos indicadores que podem ser recolhidos da solução. Actualmente, consideram-se os seguintes indicadores:

* Número de serviços
* Custo computacional
* Número de blocos não cobertos
* Número de blocos sobrecobertos
* Total do tempo de trabalho (sem serviços *Bocado*)
* Média do tempo de trabalho (sem serviços *Bocado*)
* Total do tempo de trabalho dos serviços *Bocado*
* Média do tempo de trabalho dos serviços *Bocado*
* Tempo computacional para resolver o modelo
* Gap % final

Outros indicadores poderão ser por exemplo:

* Número de ninhos de rato na solução
* tempo total dos blocos não cobertos.
* Número de serviços de viatura com blocos por cobrir
* Número de mudanças de viatura


.. rubric:: 2) Indicadores por tipologia de serviço tripulante

Para cada tipologia activa apresenta-se a seguinte informação:

* Número de serviços gerados
* Número de serviços utilizados na solução
* A percetagem em relação ao total de serviços utilizados na solução
* *Delta* representa a diferença para o limite (inferior ou seperior) desejado. O *Delta* apenas existe se o número de serviços for menor que o mínimo ou maior do que o máximo.
* Tempo de trabalho total
* Tempo de trabalho médio

Outros indicadores que também podem ser tidos em conta:

* Total horas extraordinárias



Nós como pontos de rendição dependente da linha
===============================================


