=================
Capítulo 4: MOADE
=================

.. _MOADE:

Introdução
==========

Aqui vai ficar a informação relativa à disciplina de MOADE

Exercicios
==========
ex2 - CD e mercados
============================

Conjuntos

.. math::
    \begin{align*}
    I &= \text{conjunto de CDs passiveis de serem abertos, } I = \{1,2,3\} \\[1em]
    J &= \text{conjunto de mercados, } J = \{1,2,3\} \\[1em]
    a_{i} &= \text{capacidade em paletes do CD } i \in I \\[1em]
    b_{j} &= \text{procura em paletes do mercado } j \in J \\[1em]
    f_{i} &= \text{investimento para instalar o CD } i \in I \\[1em]
    c_{ij} &= \text{custo de transporte por palete do CD } i \in I \text{ para o mercado } j \in J \\[1em]
    y_{i} &= \text{1 se o CD } i \in I \text{ é instalado, 0 c.c.} \\[1em]
    x_{ij} &= \text{quantidade de paletes transportadas do CD } i \in I \text{ para o mercado } j \in J
    \end{align*}


.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}f_i y_i  + \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{j \in J} x_{ij} \le a_i y_i       &   \quad \forall  i \in I      \\
    &                       & \quad \sum_{i \in I} x_{ij} =  b_j            &   \quad \forall  j \in J      \\
    &                       & \quad \sum_{i \in I} y_i = 2                  &   \quad \forall  j \in J      \\
    &                       & \quad y_i \in \{0,1\}                         &   \quad \forall  i \in I      \\
    &                       & \quad x_{ij} \in  \mathbb{Z}^{+}_{0}          &   \quad \forall  i \in I, j \in J

ex3 - Máquinas a preparar
============================

Conjuntos

.. math::
    \begin{align*}
    I &= \text{conjunto de máquinas a preparar, } I = \{1,2,3\} \\[1em]
    f_{i} &= \text{custo de preparação da máquina } i \in I \\[1em]
    c_{i} &= \text{custo de produção/peça na máquina } i \in I \\[1em]
    a_{i} &= \text{capacidade de produção máxima da máquina } i \in I \\[1em]
    m &= \text{minimo de unidades a produzir se uma máquina é preparada}\\[1em]
    y_{i} &= \text{1 se a máquina } i \in I \text{ é preparada para produção, 0 c.c.} \\[1em]
    x_{i} &= \text{número de peças produzidas pela máquina } i \in I
    \end{align*}


.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}f_i y_i  + \sum_{i \in I}\sum_{j \in J} c_{i}x_{i} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{i \in I} x_{i} \ge 2000           &   \quad \forall  i \in I      \\
    &                       & x_{i} \le  a_i y_i                            &   \quad \forall  i \in I      \\[1em]
    &                       & \quad x_i \ge m y_i                           &   \quad \forall  i \in I      \\[1em]
    &                       & \quad y_i \in \{0,1\}                         &   \quad \forall  i \in I      \\
    &                       & \quad x_{i} \in  \mathbb{Z}^{+}_{0}           &   \quad \forall  i \in I



ex4 - Furos
============================

Conjuntos

.. math::
    \begin{align*}
    I &= \text{conjunto de locais onde perfurar, } I = \{1,2\} \\[1em]
    J &= \text{conjunto de alvos } J = \{1,2,3,4\} \\[1em]
    f_{i} &= \text{custo de preparação em cada local } i \in I \\[1em]
    c_{ij} &= \text{custo de furar o alvo } j \in J \text{ no local } i \in I \\[1em]
    y_{i} &= \text{1 se o local } i \in I \text{ é escolhido, 0 c.c.} \\[1em]
    x_{ij} &= \text{1 se o alvo } j \in J \text{ localizado no local } i \in I \text{ é selecionado, 0 c.c.}
    \end{align*}


.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}f_i y_i  + \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{i \in I} y_{i} = 1                &                             \\
    &                       & \quad \sum_{j \in J} x_{ij} =  4y_i              &   \quad \forall  i \in I      \\[1em]
    &                       & \quad y_i \in \{0,1\}                         &   \quad \forall  i \in I      \\
    &                       & \quad x_{ij} \in \{0,1\}                      &   \quad \forall  i \in I, j \in J


ex4 - Furos2
============================

Conjuntos

.. math::
    \begin{align*}
    I &= \text{conjunto de locais onde perfurar, } I = \{1,2\} \\[1em]
    J &= \text{conjunto de alvos } J = \{1,2,3,4\} \\[1em]
    f_{i} &= \text{custo de preparação em cada local } i \in I \\[1em]
    c_{ij} &= \text{custo de furar o alvo } j \in J \text{ no local } i \in I \\[1em]
    p_{ij} &= \text{probabilidade de explosão no alvo } j \in J \text{ no local } i \in I \\[1em]
    y_{i} &= \text{1 se o local } i \in I \text{ é escolhido, 0 c.c.} \\[1em]
    x_{ij} &= \text{1 se o alvo } j \in J \text{ localizado no local } i \in I \text{ é selecionado, 0 c.c.}
    \end{align*}


.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}\sum_{j \in J} p_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{i \in I} y_{i} = 1                                                    &                                   \\[1em]
    &                       & \quad \sum_{j \in J} x_{ij} \le  4y_i                                             &   \quad \forall  i \in I          \\[1em]
    &                       & \quad \sum_{j \in J} x_{ij} \ge  2y_i                                              &   \quad \forall  i \in I          \\[1em]
    &                       & \quad \sum_{i \in I}f_i y_i  + \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} \le 15   &   \quad \forall  i \in I          \\[1em]
    &                       & \quad y_i \in \{0,1\}                                                             &   \quad \forall  i \in I          \\
    &                       & \quad x_{ij} \in \{0,1\}                                                          &   \quad \forall  i \in I, j \in J



Exemplo TLDRT
=============

.. math::
    \begin{align*}
    I &= \text{conjunto de CDs passiveis de serem abertos, } I = \{1,2,3\} \\[1em]
    J &= \text{conjunto de mercados, } J = \{1,2,3\} \\[1em]
    a_{i} &= \text{capacidade em paletes do CD } i \in I \\[1em]
    b_{j} &= \text{procura em paletes do mercado } j \in J \\[1em]
    f_{i} &= \text{investimento para instalar o CD } i \in I \\[1em]
    c_{ij} &= \text{custo de transporte por palete do CD } i \in I \text{ para o mercado } j \in J \\[1em]
    y_{i} &= \text{1 se o CD } i \in I \text{ é instalado, 0 c.c.} \\[1em]
    x_{ij} &= \text{quantidade de paletes transportadas do CD } i \in I \text{ para o mercado } j \in J
    \end{align*}


.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}f_i y_i  + \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{j \in J} x_{ij} \le a_i y_i       &   \quad \forall  i \in I      \\
    &                       & \quad \sum_{i \in I} x_{ij} =  b_j            &   \quad \forall  j \in J      \\
    &                       & \quad \sum_{i \in I} y_i = 2                  &   \quad \forall  j \in J      \\
    &                       & \quad y_i \in \{0,1\}                         &   \quad \forall  i \in I      \\
    &                       & \quad x_{ij} \in  \mathbb{Z}^{+}_{0}          &   \quad \forall  i \in I, j \in J



Trabalho MOADE
==============

Conjuntos

.. math::

    \begin{align*}
    L   &= \text{conjunto de fornecedores} \\
    I   &= \text{conjunto de Centros de Distribuição (CD)} \\
    K   &= \text{conjunto de bases logísticas} \\
    G   &= \text{conjunto de cargas/produtos}, \ G = \{GN, GP\} \\
    GN  &= \text{conjunto dos diferentes tipos de carga do tipo granel sólido} \\
    GP  &= \text{conjunto dos diferentes tipos de carga do tipo carga geral} \\
    P   &= \text{conjunto das diferentes classificações de camiões quanto ao tipo de carga a transportar } P=\{0,1\} \\
        &\text{0-camiões para transportar graneis sólidos e 1-camiões para transportar carga geral}.
    \end{align*}





Coeficientes técnicos

.. math::
    \begin{align*}
    q_{lg} &= \text{carga } g \in G \text{ produzida pelo fornecedor } l \in L
    \end{align*}


Variaveis de decisão

.. math::
    \begin{align*}
    y_i     &= \text{1 se o CD é instalado, 0 c.c} \\
    x_{lig} &= \text{carga } g \in G \text{ a transportar do fornecedor } l \in L \text{ para o CD } i \in I \\
    w_{ikg} &= \text{carga } g \in G \text{ a transportar do CD } i \in I \text{ para a base logistica } k \in K
    \end{align*}


Toda a carga :math:`g \in G` produzida pelo fronecedor :math:`l \in L`, definido como :math:`q_{lg}` deve ser destinado
a um CD :math:`i \in I` que tem de ser instalado. A quantidade de carga :math:`g \in G` que tem de ser transportada do
fornecedor :math:`l \in L` para o centro de distribuição :math:`i \in I`, é representado por :math:`X_{lig}`.
Para transportar a carga por completo é necessário ter :math:`\sigma_{lip}` camiões do tipo :math:`p \in P` com capacidade
:math:`cc` toneladas.

Cada CD pode enviar uma quantidade :math:`w_{ikg}` de carga nele armazenados para uma base logistica :math:`k \in K`,
sendo para isso necessário :math:`\delta_{ikg}` camiões de tipo :math:`p \in P` com capacidade :math:`cc`




Problema do caminho mais curto
==============================


Problema de transportes
=======================

ex2 - CD e mercados
============================

Conjuntos

.. math::
    \begin{align*}
    I &= \text{conjunto de fabricas } I = \{A,B\} \\[1em]
    J &= \text{conjunto de armazens, } J = \{1,2,3\} \\[1em]
    a_{i} &= \text{oferta na fabrica } i \in I \\[1em]
    b_{j} &= \text{procura do armazem } j \in J \\[1em]
    c_{ij} &= \text{custo de transporte por unidade da fabrica } i \in I \text{ para o armazem } j \in J \\[1em]
    x_{ij} &= \text{quantidade a transportar da fábrica } i \in I \text{ para o armazem } j \in J
    \end{align*}


.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{j \in J} x_{ij} \le a_i           &   \quad \forall  i \in I      \\
    &                       & \quad \sum_{i \in I} x_{ij} =  b_j            &   \quad \forall  j \in J      \\
    &                       & \quad x_{ij} \ge 0                            &   \quad \forall  i \in I, j \in J


.. math::
    &\mbox{ minimizar }     & \quad Z = 4x_{A1} + 7x_{A2} + 6x_{A3} + 9x_{B1} + 5x_{B2} + 5x_{B3} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & x_{A1} + x_{A2} + x_{A3} \le 800          &        \\
    &                       & x_{B1} + x_{B2} + x_{B3} \le 700          &         \\
    &                       & x_{A1} + x_{B1}  = 600            &        \\
    &                       & x_{A2} + x_{B2}  = 500            &       \\
    &                       & x_{A3} + x_{B3}  = 300            &        \\
    &                       & \quad x_{A1}, x_{A2}, x_{A3}, x_{B1}, x_{B2}, x_{B3} \ge 0



Exercicios Programação por metas
================================

lfjdhf

.. math::
    \begin{align*}
    I &= \text{conjunto de produtos } I = \{1,2\} \\[1em]
    J &= \text{conjunto de metas a atingir } I = \{1,2,3\} \\[1em]
    a_{i} &= \text{numero de h.m necessarias para produzir o produto } i \in I \\[1em]
    b_{i} &= \text{numero de h.h necessarias para produzir o produto } i \in I \\[1em]
    x_{i} &= \text{quantidade a produzir do produto } i \in I \\[1em]
    d_{j}^{+} &= \text{desvio por excesso relativamente à meta } j \in J \\[1em]
    d_{j}^{-} &= \text{desvio por defeito relativamente à meta } j \in J
    \end{align*}

.. math::
    &\mbox{ minimizar }     & \quad Z = 4x_{A1} + 7x_{A2} + 6x_{A3} + 9x_{B1} + 5x_{B2} + 5x_{B3} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 3x_{1} + 2x_{2} \le 60          &        \\
    &                       & x_{B1} + x_{B2} + x_{B3} \le 700          &         \\
    &                       & x_{A1} + x_{B1}  = 600            &        \\
    &                       & x_{A2} + x_{B2}  = 500            &       \\
    &                       & x_{A3} + x_{B3}  = 300            &        \\
    &                       & \quad x_{A1}, x_{A2}, x_{A3}, x_{B1}, x_{B2}, x_{B3} \ge 0




Exercicios Programação por metas
================================

lfjdhf

.. math::
    \begin{align*}
    I &= \text{conjunto de produtos } I = \{1,2\} \\[1em]
    J &= \text{conjunto de metas a atingir } J = \{1,2,3\} \\[1em]
    a_{i} &= \text{numero de h.m necessarias para produzir o produto } i \in I \\[1em]
    b_{i} &= \text{numero de h.h necessarias para produzir o produto } i \in I \\[1em]
    x_{i} &= \text{quantidade a produzir do produto } i \in I \\[1em]
    d_{j}^{+} &= \text{desvio por excesso relativamente à meta } j \in J \\[1em]
    d_{j}^{-} &= \text{desvio por defeito relativamente à meta } j \in J
    \end{align*}

.. math::
    &\mbox{ minimizar }     & \quad Z = ... &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 3x_{1} + 2x_{2} \le 60          &        \\[1em]
    &                       & x_{1} + 2x_{2} \le 40          &         \\[1em]
    &                       & 5x_{1} + 2x_{2}  \ge 50            &        \\[1em]
    &                       & x_{1} = 15            &


Novo modelo com metas

.. math::
    &\mbox{ minimizar }     & \quad Z = d_{1}^{-} + d_{2}^{+} + d_{3}^{+} + d_{3}^{-}  &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 3x_{1} + 2x_{2} \le 60          &        \\[1em]
    &                       & x_{1} + 2x_{2} + d_{2}^{-} - d_{2}^{+} = 40          &         \\[1em]
    &                       & 5x_{1} + 2x_{2} + d_{1}^{-} - d_{1}^{+} = 50            &        \\[1em]
    &                       & x_{1} + d_{3}^{-} - d_{3}^{+}= 15            & \\[1em]
    &                       & \quad x_{i} \in \mathbb{Z}^{+}_{0}      &  \quad \forall  i \in I \\[1em]
    &                       & \quad d_{j}^{-},d_{j}^{+} \ge 0      &  \quad \forall  j \in J


Dado os resultados, a empresa decidiu alterar a meta 2, pretendendo agora que se utilize da melhor forma possível a mão
de obra na Secção 2 (h.h), sem recorrer nem a substituição de tarefas (), nem exigência de horas extraordinárias


.. math::
    &\mbox{ minimizar }     & \quad Z = d_{1}^{-}  &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 3x_{1} + 2x_{2} \le 60          &        \\[1em]
    &                       & 5x_{1} + 2x_{2} + d_{1}^{-} - d_{1}^{+} = 50            &        \\[1em]
    &                       & \quad x_{i} \in \mathbb{Z}^{+}_{0}      &  \quad \forall  i \in I \\[1em]
    &                       & \quad d_{1}^{-},d_{1}^{+} \ge 0      &

Segunda iteração

.. math::
    &\mbox{ minimizar }     & \quad Z = d_{2}^{+}  &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 3x_{1} + 2x_{2} \le 60          &        \\[1em]
    &                       & x_{1} + 2x_{2} + d_{2}^{-} - d_{2}^{+} = 40          &         \\[1em]
    &                       & 5x_{1} + 2x_{2} + d_{1}^{-} - d_{1}^{+} = 50            &        \\[1em]
    &                       & d_{1}^{-} \le 0            &        \\[1em]
    &                       & \quad x_{i} \in \mathbb{Z}^{+}_{0}      &  \quad \forall  i \in I \\[1em]
    &                       & \quad d_{2}^{-},d_{2}^{+} \ge 0      &


terceira iteração

.. math::
    &\mbox{ minimizar }     & \quad Z = d_{3}^{+} + d_{3}^{-}  &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 3x_{1} + 2x_{2} \le 60          &        \\[1em]
    &                       & x_{1} + 2x_{2} + d_{2}^{-} - d_{2}^{+} = 40          &         \\[1em]
    &                       & 5x_{1} + 2x_{2} + d_{1}^{-} - d_{1}^{+} = 50            &        \\[1em]
    &                       & x_{1} + d_{3}^{-} - d_{3}^{+}= 15            & \\[1em]
    &                       & d_{1}^{-} \le 0            &        \\[1em]
    &                       & d_{2}^{+} \le 0            &        \\[1em]
    &                       & \quad x_{i} \in \mathbb{Z}^{+}_{0}      &  \quad \forall  i \in I \\[1em]
    &                       & \quad d_{3}^{-},d_{3}^{+} \ge 0      &


DEWRIGHT COMPANY – Part I
=========================

Modelo generico

.. math::
    \begin{align*}
    I &= \text{conjunto de produtos } I = \{1,2,3\} \\[1em]
    J &= \text{conjunto de metas a atingir } J = \{1,2,3\} \\[1em]
    a_{i} &= \text{lucro/un (milhoes)  produzida do produto } i \in I \\[1em]
    b_{i} &= \text{numero/un (centenas) empregados para produzir o produto } i \in I \\[1em]
    c_{i} &= \text{investimento/un (milhoes) para produzir o produto } i \in I \\[1em]
    p^*_{j} &= \text{penalidade por unidade de desvio * ao objectivo } j \in J \\[1em]
    x_{i} &= \text{quantidade a produzir do produto } i \in I \\[1em]
    d_{j}^{+} &= \text{desvio por excesso relativamente à meta } j \in J \\[1em]
    d_{j}^{-} &= \text{desvio por defeito relativamente à meta } j \in J
    \end{align*}


Restrições

.. math::
    &\mbox{ minimizar }     & \quad Z = 5d_{1}^{-} + 2d_{2}^{+} + 4d_{2}^{-} + 3d_{3}^{+} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 12x_1 + 9x_2 +  15x_3 \ge = 125          &        \\[1em]
    &                       & 5x_1 + 3x_2 + 4x_3 = 40           &         \\[1em]
    &                       & 5x_1 + 7x_2 + 8x_3 \le 55           &        \\[1em]
    &                       & x_i, d^+_j, d^-_j \ge 0 & \quad \forall i \in I, j \in J



.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{j \in J} p^*_j d^*_j &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{i \in I} a_i x_i + d_{1}^{-} - d_{1}^{+} = 125          &        \\
    &                       & \sum_{i \in I} b_i x_i + d_{2}^{-} - d_{2}^{+} = 40           &         \\
    &                       & \sum_{i \in I} c_i x_i + d_{3}^{-} - d_{3}^{+} = 55           &        \\
    &                       & x_i, d^*_j \ge 0 & \quad \forall i \in I, j \in J

.. math::
    &\mbox{ minimizar }     & \quad Z = 5d_{1}^{-} + 2d_{2}^{+} + 4d_{2}^{-} + 3d_{3}^{+} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 12x_1 + 9x_2 +  15x_3 + d_{1}^{-} - d_{1}^{+} = 125          &        \\[1em]
    &                       & 5x_1 + 3x_2 + 4x_3 + d_{2}^{-} - d_{2}^{+} = 40           &         \\[1em]
    &                       & 5x_1 + 7x_2 + 8x_3 + d_{3}^{-} - d_{3}^{+} = 55           &        \\[1em]
    &                       & x_i, d^+_j, d^-_j \ge 0 & \quad \forall i \in I, j \in J


Formulação da segunda iteração assumindo

.. math::
    &\mbox{ minimizar }     & \quad Z = 2d_{2}^{+} + 4d_{2}^{-}&       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & 12x_1 + 9x_2 +  15x_3 + d_{1}^{-} - d_{1}^{+} = 125          &        \\[1em]
    &                       & 5x_1 + 3x_2 + 4x_3 + d_{2}^{-} - d_{2}^{+} = 40           &         \\[1em]
    &                       & d_{1}^{-} \le 3           &        \\[1em]
    &                       & x_i, d^+_j, d^-_j \ge 0 & \quad \forall i \in I, j \in \{1,2\}


Trabalho
========

O artigo propõe um modelo matemático para estruturar a rede logística em 3 níveis: i) fronercedores; ii)centgros de distribuição (CD), como infraestruturas intermédias;
iii) bases logisticas.

Modelo
------

O objectivo é minimizar os custos fixos de implementação dos CD, os custos de operação dessas infraestruturas, e os custos de transporte entre as instalações na rede.

**Conjuntos**

.. math::
    \begin{align*}
    L &= \text{conjunto de fornecedores } L = \{1,..., 9\} \\[1em]
    I &= \text{conjunto de centros distribuição } J = \{1,...,8\} \\[1em]
    K &= \text{conjunto de bases logísticas } K = \{1,2,3\} \\[1em]
    GN &= \text{conjunto de diferentes tipos do tipo granel sólido } \\[1em]
    GP &= \text{conjunto de diferentes tipos do tipo granel geral } \\[1em]
    G &= \text{conjunto de diferentes tipos de carga } G = GN \cup GP \\[1em]
    P &= \text{conjunto das diferentes classificações de maioes quanto ao tipo de carga a transportar }
    \end{align*}

**Parametros**

.. math::
    \begin{align*}
    q_{lg} &= \text{oferta do fornecedore } l \in l \text{ do tipo } g \in G \\[1em]
    b_{kg} &= \text{procura da base logistica } k \in K \text{ da carga do tipo } g \in G\\[1em]
    cap_{i} &= \text{capacidade do CD } i \in I \\[1em]
    d_{li} &= \text{distância entre o fornecedor } l \in L \text{ e o CD } i \in I \\[1em]
    d_{ik} &= \text{distância entre o CD } i \in I \text{ e a base logistica } k \in K
    \end{align*}

**Variaveis de decisão**

.. math::
    \begin{align*}
    y_{i} &= \text{1 se o CD } i \in I \text{ é instalado, 0 c.c.} \\[1em]
    x_{lig} &= \text{qtd do fornecedor } l \in L \text{ para o CD } i \in I \text{do tipo } g \in G \\[1em]
    w_{ikg} &= \text{qtd do CD } i \in I \text{ para o CD } i \in I \text{do tipo } g \in G\\[1em]
    s_{lig} &= \text{qtd de veiculos do fornecedor } l \in L \text{ para o CD } i \in I \text{do tipo } g \in G\\[1em]
    d_{ikg} &= \text{qtd de veiculos do CD } i \in I \text{ para a BL } k \in K \text{do tipo } g \in G
    \end{align*}


**Modelo**

.. math::
    &\mbox{ minimizar }     & \quad Z = \sum_{i \in I}f_i y_i  + \sum_{i \in I}o_i y_i      \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \quad \sum_{i \in I} x_{lig} = q_{ig}                         &   \quad \forall  l \in L      \\
    &                       & \quad \sum_{i \in I} w_{ikg} =  x_{lig}                       &   \quad \forall  i \in I      \\
    &                       & \quad \sum_{l \in L}\sum_{g \in G} x_{lig} \le y_{i}cap_{i}   &   \quad \forall  i \in I      \\
    &                       & \quad \sum_{i \in I} w_{ikg} = b_{kg}                          &   \quad \forall  k \in K, g \in G     \\
    &                       & \quad y_i \in \{0,1\}                         &   \quad \forall  i \in I      \\
    &                       & \quad x_{ij} \in  \mathbb{Z}^{+}_{0}          &   \quad \forall  i \in I, j \in J



A restição 1 representa a restrição da oferta para cada tipo de carga :math:`g \in G`  em cada um dos fornecedores :math:`l \in L`.

A restrição 2 é dedicada aos CD e diz que , para cada CD, a quantidade transportada de cada tipo  vinda dos fornecedores é igual à enviada do CD para as BL. Isto significa que não existe armazenagem nos centros de distribuição (à semana)




Problema afetação
=================

.. math::
    \begin{align*}
    I &= \text{conjunto de carpinteiros} \\[1em]
    J &= \text{conjunto de objectos } \\[1em]
    c_{ij} &= \text{tempo do carpinteiro } i \in I \text{ produzir o objecto } j \in J\\[1em]
    x_{ij} &= \text{1 se o carpinteiro } i \in I \text{ produz o objecto } j \in J \text{, 0 c.c}
    \end{align*}

.. math::
    &\mbox{ min }     & \quad Z = \sum_{i \in I}\sum_{j \in J} c_{ij}x_{ij} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{j \in J} x_{ij} = 1     &  \quad \forall  i \in I     \\
    &                       & \sum_{i \in I} x_{ij} = 1     &  \quad \forall  j \in J     \\
    &                       & \quad x_{ij} \in \{0,1\}      &  \quad \forall  i \in I, j \in J


.. math::
    &\mbox{ min }     & \quad Z =  &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{j \in J} x_{ij} = 1     &  \quad \forall  i \in I     \\
    &                       & \sum_{i \in I} x_{ij} = 1     &  \quad \forall  j \in J     \\
    &                       & \quad x_{ij} \in \{0,1\}      &  \quad \forall  i \in I, j \in J



Problema da mochila
===================

.. math::
    \begin{align*}
    I &= \text{conjunto de objectos} \\[1em]
    v_{i} &= \text{valor do objecto } i \in I\\[1em]
    p_{i} &= \text{peso do objecto } i \in I\\[1em]
    a_{i} &= \text{volume do objecto } i \in I\\[1em]
    capP &= \text{capacidade em peso}\\[1em]
    capV &= \text{capacidade em volume}\\[1em]
    x_{i} &= \text{1 se levamos o objecto } i \in I \text{, 0 c.c}
    \end{align*}

.. math::
    &\mbox{ max }     & \quad Z = \sum_{i \in I} v_{i}x_{i} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{i \in I} p_i x_{i} \le capP     &       \\
    &                       & \sum_{i \in I} a_i x_{i} \le capV     &      \\
    &                       & \quad x_{i} \in \{0,1\}      &  \quad \forall  i \in I


.. math::
    &\mbox{ max }     & \quad Z = \sum_{i \in I}\sum_{j \in J} v_{ij}x_{i} &       \\
    \\[1pt]   % Smaller space
    &\mbox{ s.a. }          & \sum_{i \in I} x_i \ge 2    &       \\
    &                       & x_1 + x_5 \le 1    &      \\
    &                       & x_2 \le x_3   &      \\
    &                       & 2x_2 \le x_4 + x_5   &      \\
    &                       & \quad x_{i} \in \{0,1\}      &  \quad \forall  i \in I




Problema de cobertura
=====================

Queremos instalar router wi-fi de forma a providenciar sinal a um conjunto de 7 prédios, para os quais se apresenta a
sua altura máxima. Temos aprovação para construir torres em 5 localizações. Para cada uma apresentamos a altura máxima
permitida da torre, e os seus custo de instalação.

Um prédio considera-se coberto se a torre wi-fi está a pelo menos 100 metros do edifício e se situa 10m acima da altura
máxima do prédio.

O objectivo é cobrir todos os prédios ao menor custo. Modele o problema de cobertura.


.. math::
    \begin{align*}
    I &= \text{conjunto torres a construir} \\[1em]
    J &= \text{conjunto edificios a cobrir} \\[1em]
    a_{ij} &= 1 \text{ se a torre } i \in I \text{ cobre o edificio } j \in J \text{, 0 c.c}\\[1em]
    x_{i} &= 1 \text{ se a torre } i \in I \text{ cobre o edificio } j \in J \text{, 0 c.c}
    \end{align*}