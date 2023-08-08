A nomenclatura dos grafos neste folder segue o padrão abaixo:

* Grafos que pertencem a certas familias são denominados como (name)(X)-(Y)-(count), onde *name* é um termo que identifica
 a família, *X* e *Y* são valores numéricos relativos a família e *count* é a ordem nesta coleção, caso exista
 mais de um exemplo para o mesmo tipo de grafo. O único parâmetro obrigatório é **name**.

* Grafos mais gerais são denominados por:

 (s|p|m)-(d|u)-(w)-(a|cy)-(sc|dis|dc)-(p)-(t)-(b)-(ch).graphml

|type | orientation	|weight	|cycle	|connection	|planarity	|tree	|partition	|chordals|
------|-------------|-------|-------|------------|----------|------|----------|---------|
|(s)imple	|(d)irect	|(w)eighted	|(a)cyclic	|(sc)trongly connected	|(p)lanar	|(t)ree	|(b)bipartite	|(ch)ordal
|(p)seudograph	|(u)ndirect	|	  |(cy)clic|	(dis)connected|	|	|	|	
|(m)ultigraph	|	|	|	 |       (wc)akly connected			| |  |	

onde os tags só são aplicados se o grafo possuir a propriedade indicada.
