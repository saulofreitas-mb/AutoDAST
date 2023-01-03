# Projeto automação de DAST 

## Resumo:

 O objetivo deste projeto é auxiliar na produção de uma ferramenta de DAST para WEB. Foi decidido que em primeiro momento serão usados os scans do OWASP ZAP dentro do github actions, permitindo a execução de scans de forma automatizada baseado em triggers definidos previamente. Embora possuam algumas restrições, são uma opção viável para uma primeira implementação. A utilização do framework de automação, que permite maior flexibilidade, pode vir a ser uma opção posteriormente. 


## Scans: 
 São disponibilizados 3 scans distintos dentro do github marketplace do OWASP, sendo estes: 
 ### Baseline Scan: 
  Utilizado para varrer aplicações WEB e procurar vulnerabilidades sem realizar ataques de forma ativa.

  - Roda o crawler do ZAP contra o alvo por padrão durante um minuto e em seguida um scan passivo. A duração do crawler pode ser reconfigurada.  
  
  - Por padrão, reporta todos alertas como warnings 
  
  
  - Esse script é pensado para ambientes de CI/CD. Porém é preciso se atentar ao viés do scan. 
  
 ### API Scan: 
  Ferramenta de DAST para realizar scans ativos em APIs. Os formatos aceitos são openapi, soap ou graphql, por padrão a ferramenta assuma formato openapi.

 ### Full Scan: 
 Utiliza O ZAP spider e opcionalmente um crawler AJAX e um scan completo contra a aplicação, explorando ativamente possíveis vetores de ataque e gerando issues dentro do repositório.

 A integração com o github actions permite que os scans sejam reportados e gerenciados através de issues dentro do repositório do projeto, gerando e eliminando-as conforme são resolvidas. 

 

## Implementação:  

 A automação de scans através do github actions se dá através de um arquivo yaml, que fica dentro da pasta .git e dita o workflow do processo. Através dele pode-se configurar os triggers para o scan, o target, e outras configurações pertinentes. Esta ferramenta pode ser configurada para repositórios públicos ou privados.
 
 