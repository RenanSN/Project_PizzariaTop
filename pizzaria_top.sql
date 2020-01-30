create database pizzariatop;
use pizzariatop;
create table tbl_usuarios(
	cod_usuario int not null auto_increment,
    login_usuario varchar(15) not null,
    senha_usuario varchar(8) not null,
	nome_usuario varchar(50) not null,
	primary key(cod_usuario));
insert into tbl_usuarios (login_usuario, senha_usuario, nome_usuario)
	values("admin","admin123","Usuario"),
    ("dba", "dba123", "Renan Santos");
select * from tbl_usuarios;
create table tbl_produtos(
	cod_produto int not null auto_increment,
    nome_produto varchar(45) not null,
    validade_produto date not null,
    gasto_produto decimal(10,2) not null,
    venda_produto decimal(10,2) not null,
    quant_produto int not null,
    primary key(cod_produto));
insert into tbl_produtos(nome_produto, validade_produto, gasto_produto, venda_produto, quant_produto) 
	values("Pizza Calabresa Grande", (now() + interval 3 day), 10.00, 25.00, 50),
		("Coca-Cola", (now() + interval 8 month), 4.00, 7.00, 50);
select * from tbl_produtos;



select * from tbl_produtos where cod_produto = 2;

