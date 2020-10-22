#Kp = 4, Ki = 0,1 e Kd = 1
Kp = 5;
Ki = 8;
Kd = 10.25;
Ts = 0.1;

SP = 1;
PV = 0;

resp_6 = 0;
AcaoIntegral = 0;
ErroAnterior = SP - PV;

tempo = 0:0.1:6;

for i = 0.1:0.1:6
  Erro = SP - PV;
  
  AcaoProporcional = Kp*Erro;
  AcaoIntegral = AcaoIntegral + Ki*Ts*Erro;
  AcaoDerivativa = ((Erro - ErroAnterior)/Ts)*Kd;
  
  ErroAnterior  = Erro;
  
  AcaoControlador = AcaoProporcional + AcaoIntegral + AcaoDerivativa;
  
  PV = 0.99736*PV + 0.0019800*AcaoControlador;
  resp_6 = [resp_6 PV];
 
end

plot (tempo,resp_6)
plot.show()