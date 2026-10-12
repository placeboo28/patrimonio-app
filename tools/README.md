# Herramientas de publicación — Gestión Patrimonio

La app se publica **cifrada** (AES-GCM, clave derivada del PIN con PBKDF2). En este repositorio no hay ningún dato en claro ni el PIN.

Para regenerar `index.html` a partir de la app sin cifrar:

```
pip install cryptography
python3 tools/build.py ruta/a/app_fuente.html <PIN>
git add index.html sw.js && git commit -m "Actualización datos" && git push
```

`sw.js` cambia de versión en cada build para que los móviles cojan la nueva.

Esta app es una copia de consulta de la app de Claude (artifact): los datos se exportan de su base de datos y se embeben con `tools/build_snapshot.py` antes de cifrar.
