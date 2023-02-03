--Select padrão para se obter os valores dentro do banco de dados.
SELECT * FROM RNR_VENDAS;
SELECT * FROM RNR_ENTREGA;

--O Calculo para se descobrir a diferença de dias é feito subtraindo-se as datas de venda e entrega. 
SELECT 15-23 FROM DUAL; ---8
SELECT 05-28 FROM DUAL; --23
SELECT 24-30 FROM DUAL; ---6
SELECT 20-27 FROM DUAL; ---7 

--A métrica utilizada para calculo da média é adicionando um grupo de números e dividindo pela contagem desses números.
SELECT 23+8+7+6 FROM DUAL; --44
SELECT 44/4 FROM DUAL; --11

--*Obtendo-se esses dados chegamos a conclusão de que se passam em média 11 dias da compra do produto até a entrega ao cliente*