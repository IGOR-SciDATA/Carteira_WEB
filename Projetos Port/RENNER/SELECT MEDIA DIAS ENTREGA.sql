--Select padr�o para se obter os valores dentro do banco de dados.
SELECT * FROM RNR_VENDAS;
SELECT * FROM RNR_ENTREGA;

--O Calculo para se descobrir a diferen�a de dias � feito subtraindo-se as datas de venda e entrega. 
SELECT 15-23 FROM DUAL; ---8
SELECT 05-28 FROM DUAL; --23
SELECT 24-30 FROM DUAL; ---6
SELECT 20-27 FROM DUAL; ---7 

--A m�trica utilizada para calculo da m�dia � adicionando um grupo de n�meros e dividindo pela contagem desses n�meros.
SELECT 23+8+7+6 FROM DUAL; --44
SELECT 44/4 FROM DUAL; --11

--*Obtendo-se esses dados chegamos a conclus�o de que se passam em m�dia 11 dias da compra do produto at� a entrega ao cliente*