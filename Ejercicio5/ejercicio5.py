from kanren import Relation, facts, run, var
padre = Relation()
madre = Relation()
abuelo = Relation()
abuela = Relation()
hermanos = Relation()
primos = Relation()
tios = Relation()

facts(padre, 
      ("Eduardo","Josue"),
      ("Eduardo", "Joaquin"),
      ("Ignacio",  "Eduardo"),
      ("Ignacio",  "Claudia"),
      ("Roberto",  "Rosario"),
      ("Roberto",  "Laura"),
      ("Ariel","Gael")
      )

facts(madre, 
      ("Rosario","Josue"),
      ("Rosario", "Joaquin"),
      ("Martha",  "Eduardo"),
      ("Martha",  "Claudia"),
      ("Maria",  "Rosario"),
      ("Maria",  "Laura"),
      ("Claudia","Gael")
      )

facts(abuelo,
      ("Ignacio","Josue"),
      ("Ignacio","Joaquin"),
      ("Roberto","Josue"),
      ("Roberto","Joaquin"),
      ("Ignacio","Gael")
      )

facts(abuela,
      ("Martha","Josue"),
      ("Martha","Joaquin"),
      ("Maria","Josue"),
      ("Maria","Joaquin"),
      ("Martha","Gael")
      )

facts(hermanos,
      ("Joaquin","Josue"),
      ("Claudia","Eduardo"),
      ("Laura","Rosario")
      )

facts(primos,
      ("Gael","Josue"),
      ("Gael","Joaquin")
      )

facts(tios,
      ("Ariel","Josue"),
      ("Claudia","Josue"),
      ("Laura","Josue"),
      ("Ariel","Joaquin"),
      ("Claudia","Joaquin"),
      ("Laura","Joaquin"),
      ("Eduardo","Gael"),
      ("Rosario","Gael"),
      )

x=var()
print(run(0,x,tios(x,"Josue")))
print(run(0,x,abuelo(x,"Josue")))
print(run(0,x,madre(x,"Josue")))
