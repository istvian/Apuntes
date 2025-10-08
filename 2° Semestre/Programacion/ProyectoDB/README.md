# Pasos

## appserv
- Buscar appserv en menu inicio
- Ejecutar en MySQLCommand Line Client

<img width="685" height="512" alt="image" src="https://github.com/user-attachments/assets/7ef96f8a-7c37-4485-8f76-6b3ed3ae7dd2" />

- Crear Base de datos = "empresa"
```sql
create database empresa;
use empresa;
```

- Crear Tablas y datos
```sql
create table Repuestos(
codRep varchar(3) not null primary key,
nomRep varchar(20),
fechaFabr date,
precioProveedor int(8),
precioVenta int(8),
peso decimal(6,2)
) engine=innodb;

insert into Repuestos values('r23','Motor tipo A1','2023/5/12',250000,270000,93.56);
insert into Repuestos values('r26','Motor tipo B1','2021/6/14',280000,310000,113.49);
insert into Repuestos values('r27','Motor tipo C3','2023/5/3',220000,250000,87.23);
insert into Repuestos values('r43','Inyector angu','2022/3/5',190000,185000,2.56);
insert into Repuestos values('r46','Inyector basal','2020/5/8',134000,140000,3.79);
insert into Repuestos values('r80','Válvula centry','2023/4/28',195000,230000,0.28);
insert into Repuestos values('r84','Válvula zenner','2022/5/21',265000,300000,0.72);

create table Ventas(
numVenta int(10) not null primary key,
codRepuesto varchar(3) not null references repuestos(codRep),
fechaVenta date,
montoVenta int(8)
)engine=innodb;

insert into ventas values(2500,'r26','2023/8/20',900000);
insert into ventas values(2501,'r43','2023/8/24',725000);
insert into ventas values(2502,'r27','2023/9/3',922000);
insert into ventas values(2503,'r84','2023/9/5',890000);

```

- Descargar 2 archivos
- [Database.py](<./Database.py>)
- [Conecta.py](<./Conecta.py>)

- Ejecutar en terminal
  ```bash
  pip install pymysql
  ```

  
