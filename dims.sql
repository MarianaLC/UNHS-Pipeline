insert into DIM_sexo(descricao) values("Unknown");
insert into DIM_sexo(descricao) values("Female");
insert into DIM_sexo(descricao) values("Male");

insert into dim_risco(descricao) values("Unknown");
insert into dim_risco(descricao) values("Late risk factors");
insert into dim_risco(descricao) values("Only risk factors");
insert into dim_risco(descricao) values("No risk factors");

/*set foreign_key_checks = 0;
truncate table fact_ranu;
set foreign_key_checks = 1;*/

insert into dim_localnascimento(descricao) values("Unknown");
insert into dim_localnascimento(descricao) values("Internal");
insert into dim_localnascimento(descricao) values("External");

insert into dim_puerperio(descricao) values("Unknown");
insert into dim_puerperio(descricao) values("Normal");
insert into dim_puerperio(descricao) values("Complicated");

insert into dim_avaliacao1(descricao) values("Unknown");
insert into dim_avaliacao1(descricao) values("Pass");
insert into dim_avaliacao1(descricao) values("Refer Both");
insert into dim_avaliacao1(descricao) values("Refer Right");
insert into dim_avaliacao1(descricao) values("Refer Left");

insert into dim_avaliacao2(descricao) values("Unknown");
insert into dim_avaliacao2(descricao) values("Pass");
insert into dim_avaliacao2(descricao) values("Refer Both");
insert into dim_avaliacao2(descricao) values("Refer Right");
insert into dim_avaliacao2(descricao) values("Refer Left");

insert into dim_avaliacao3(descricao) values("Unknown");
insert into dim_avaliacao3(descricao) values("Pass");
insert into dim_avaliacao3(descricao) values("Refer Both");


insert into dim_apgar1(descricao) values("Unknown");
insert into dim_apgar1(descricao) values(0);
insert into dim_apgar1(descricao) values(1);
insert into dim_apgar1(descricao) values(2);
insert into dim_apgar1(descricao) values(3);
insert into dim_apgar1(descricao) values(4);
insert into dim_apgar1(descricao) values(5);
insert into dim_apgar1(descricao) values(6);
insert into dim_apgar1(descricao) values(7);
insert into dim_apgar1(descricao) values(8);
insert into dim_apgar1(descricao) values(9);
insert into dim_apgar1(descricao) values(10);

insert into dim_apgar5(descricao) values("Unknown");
insert into dim_apgar5(descricao) values(0);
insert into dim_apgar5(descricao) values(1);
insert into dim_apgar5(descricao) values(2);
insert into dim_apgar5(descricao) values(3);
insert into dim_apgar5(descricao) values(4);
insert into dim_apgar5(descricao) values(5);
insert into dim_apgar5(descricao) values(6);
insert into dim_apgar5(descricao) values(7);
insert into dim_apgar5(descricao) values(8);
insert into dim_apgar5(descricao) values(9);
insert into dim_apgar5(descricao) values(10);

insert into dim_fator1(descricao) values("Family history of congenital sensorineural hearing loss");
insert into dim_fator1(descricao) values("No risk factor");
insert into dim_fator2(descricao) values("Congenital infectious disease");
insert into dim_fator2(descricao) values("No risk factor");
insert into dim_fator3(descricao) values("Congenital anomaly of face");
insert into dim_fator3(descricao) values("No risk factor");
insert into dim_fator4(descricao) values("Hyperbilirubinemia");
insert into dim_fator4(descricao) values("No risk factor");
insert into dim_fator5(descricao) values("Low birth weight infant");
insert into dim_fator5(descricao) values("No risk factor");
insert into dim_fator6(descricao) values("Ototoxic medication");
insert into dim_fator6(descricao) values("No risk factor");
insert into dim_fator7(descricao) values("Bacterial meningitis");
insert into dim_fator7(descricao) values("No risk factor");
insert into dim_fator8(descricao) values("Apgar at 1 minute and at 5 min");
insert into dim_fator8(descricao) values("No risk factor");
insert into dim_fator9(descricao) values("Artificial respiration");
insert into dim_fator9(descricao) values("No risk factor");
insert into dim_fator10(descricao) values("Deafness symptom");
insert into dim_fator10(descricao) values("No risk factor");

select id from DIM_sexo where descricao = "Female";

select * from dim_apgar1;
select * from fact_ranu;
select * from dim_fator1;
select * from dim_fator2;
select * from dim_fator4;
/*select * from dim_sexo;
select * from dim_rastreio;
select * from dim_localnascimento;
select * from dim_puerperio;
select * from dim_risco;
select * from dim_avaliacao1;
select * from dim_avaliacao2;
select * from dim_avaliacao3;
select * from dim_apgar1;
select * from dim_apgar5;
select * from dim_rastreio;*/
