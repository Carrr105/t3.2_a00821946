# Tarea 3.2 de Diseño de Compiladores (grupo 2)

Carlos Gerardo Herrera Cortina - A00821946

Comandos para flex & bison:
```
flex scanner.l
bison -dy parser.y
gcc lex.yy.c y.tab.c -o mycompiler
./mycompiler
```

Para PLY ejecutar:
```
python3 lexyacc.py
```