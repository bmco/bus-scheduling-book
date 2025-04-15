==================================
Capítulo 3: TRLDT
==================================

.. _TRLDT:

Introdução
================================================================================

Esta pagina serve para guardar informação sbre a cadeira de TRLDT.
Aqui apresentm-se os modelos e problemas que se vão abordar.


Problema afetação
=================

.. math::
    \begin{align*}
    I &= \text{conjunto de entidades (trabalhadores)} \\[1em]
    J &= \text{conjunto de tarefas } \\[1em]
    c_{ij} &= \text{valor se a entidade } i \in I \text{ é afeta à tarefa } j \in J\\[1em]
    x_{ij} &= \text{1 se a entidade } i \in I \text{ é afeta à tarefa } j \in J \text{, 0 c.c}
    \end{align*}

.. math::
    &\mbox{ min/max }     & \quad Z = \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{j \in J} x_{ij} \le 1     &  \quad \forall  i \in I     \\
    &                       & \sum_{i \in I} x_{ij} = 1     &  \quad \forall  j \in J     \\
    &                       & \quad x_{ij} \in \{0,1\}      &  \quad \forall  i \in I, j \in J


Problema caminho mais curto
===========================

.. math::
    \begin{align*}
    N &= \text{conjunto de nós } \\[1em]
    A &= \text{conjunto de arcos } (i,j) \text{ que ligam o no } i \text{ ao no } j : i,j \in N  \\[1em]
    S &= \text{origem} \\[1em]
    T &= \text{destino} \\[1em]
    d_{ij} &= \text{distância associada ao arco } (i,j) \in A\\[1em]
    x_{ij} &= \text{1 se o arco } (i,j) \in A \text{ é escolhido, e 0 c.c}
    \end{align*}

.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{(i,j) \in A} d_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{j \in N : (i,j) \in A} x_{ij} - \sum_{j \in N : (j,i) \in A} x_{ji} = 1          &  \quad i = S  \\[1em]
    &                       & \sum_{j \in N : (j,i) \in A} x_{ji} - \sum_{j \in N : (i,j) \in A} x_{ij} = 1          &  \quad i = T  \\[1em]
    &                       & \sum_{j \in N : (i,j) \in A} x_{ij} - \sum_{j \in N : (j,i) \in A} x_{ji} = 0          &  \quad i \neq \{S,T\}  \\[1em]
    &                       & \quad x_{ij} \in \{0,1\} &  \quad \forall (i,j) \in A  \\[1em]


Problema VRP
============


.. math::
    \begin{align*}
    D &= \text{deposito} \\[1em]
    C &= \text{conjunto de clientes} \\[1em]
    N &= \text{conjunto de Nos, } N = D \cup C \\[1em]
    a_i &= \text{procura do cliente } i \in C \\[1em]
    cap &= \text{capacidade dos veículos} \\[1em]
    d_{ij} &= \text{distância associada ao arco que liga ao nó } i \in N \text{ ao nó } i \in N \\[1em]
    x_{ij} &= \text{1 se o arco que liga o local } i \in I \text{ ao local } j \in J \text{ é escolhido, 0 c.c} \\[1em]
    f_{ij} &= \text{quantidade transportada na ligação entre o local } i \in I \text{ e o local } j \in J
    \end{align*}

.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in N}\sum_{j \in N}  d_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{j \in N} x_{ij} = 1                             &  \quad i \in C            \\[1em]
    &                       & \sum_{j \in N} x_{ji} = 1                             &  \quad i \in C            \\[1em]
    &                       & \sum_{j \in N} x_{ji} - \sum_{j \in N} x_{ij}  = 0  &  \quad i \in C            \\[1em]
    &                       & f_{ji} \le  x_{ij}    cap                             &  \quad i,j \in N          \\[1em]
    &                       & \quad x_{ij} \in \{0,1\}                              &  \quad \forall i,j \in N  \\[1em]
    &                       & \quad f_{ij} \in \mathbb{Z}^{+}_{0}                   &  \quad \forall i,j \in N



