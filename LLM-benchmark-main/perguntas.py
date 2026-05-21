from pergunta import Pergunta

originais_ingles = [
    Pergunta("A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. How much does the ball cost?", "5 cents", "10 cents", "2005"),
    Pergunta("If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?", "5 minutes", "100 minutes", "2005"),
    Pergunta("In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half of the lake?", "47 days", "24 days", "2005"),
    Pergunta("If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how long would it take them to drink one barrel of water together?", "4 days", "9 days", "2014"),
    Pergunta("Jerry received both the 15th highest and the 15th lowest mark in the class. How many students are in the class?", "29 students", "30 students", "2014"),
    Pergunta("A man buys a pig for £60, sells it for £70, buys it back for £80, and sells it finally for £90. How much has he made?", "20", "10", "2014"),
    Pergunta("Simon decided to invest £8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks he had purchased were down 50%. Fortunately for Simon, from July 17 to October 17, the stocks he had purchased went up 75%. At this point, Simon has: A. broken even in the stock market. B. is ahead of where he began. C. has lost money", "C (£7000)", "B", "2014"),
    Pergunta("If you're running a race and you pass the person in second place, what place are you in?", "2nd", "1st", "2016"),
    Pergunta("A farmer had 15 sheep and all but 8 died. How many are left?", "8", "7", "2016"),
    Pergunta("Emily's father had three daughters. The first two are named April and May. What is the third daughter's name?", "Emily", "June", "2016"),
    Pergunta("How many cubic feet of dirt are there in a hole that 3 feet deep x 3 feet wide x 3 feet long?", "None", "27", "2016"),
]

originais_portugues = [
    Pergunta("Um taco e uma bola custam $1,10 no total. O taco costa um dólar a mais que a bola. Quanto custa a bola?", "5 centavos", "10 centavos", "2005"),
    Pergunta("Se 5 máquinas levam 5 minutos para produzir 5 ferramentas, quanto tempo levaria para que 100 máquinas produzissem 100 ferramentas?", "5 minutos", "100 minutos", "2005"),
    Pergunta("Em um lago há um canteiro de vitórias-régias. Todo dia esse canteiro dobra de tamanho. Se o canteiro leva 48 dias para cobrir o lago inteiro, quanto tempo levaria para que ele cobrisse metade do lago?", "47 dias", "24 dias", "2005"),
    Pergunta("Se João consegue beber um galão de água em 6 dias e Maria consegue beber um galão de água em 12 dias, quanto tempo levaria para que os dois bebessem um galão de água juntos?", "4 dias", "9 dias", "2014"),
    Pergunta("José recebeu a 15ª maior nota e a 15ª menor nota de sua turma. Quantos alunos fazem parte desta turma?", "29 alunos", "30 alunos", "2014"),
    Pergunta("Um homem compra um porco por R$60, vende-o por R$70, compra-o de volta por R$80, e vende-o de vez por R$90. Quanto lucro ele obteve?", "20", "10", "2014"),
    Pergunta("Simon decidiu investir R$8000 no mercado de ações em um dia no início de 2008; Seis meses após o investimento, no dia 17 de Julho, as ações que ele havia comprado haviam caído 50%. Para a sorte de Simon, de 17 de Julho até 17 de Outubro, as ações que ele havia comprado subiram 75%. Nesse ponto, Simon: A. Está no mesmo ponto em que começou. B. Ganhou dinheiro. C. Perdeu dinheiro.", "C (R$7000)", "B", "2014"),
    Pergunta("Se você está participando de uma corrida e ultrapassa a pessoa que está em segundo lugar, qual é a sua posição?", "Segundo", "Primeiro", "2016"),
    Pergunta("Um fazendeiro tinha 15 ovelhas e todas menos oito morreram. Quantas ovelhas sobraram?", "8", "7", "2016"),
    Pergunta("O pai de João tinha três filhos. Os dois primeiros se chamavam Abril e Maio. Qual o nome do terceiro filho?", "João", "Junho", "2016"),
    Pergunta("Quantos metros cúbicos de terra tem um buraco que possui 3 metros de profundidade, 3 metros de largura e 3 metros de comprimento?", "Nenhum", "27", "2016"),
]

originais_ex_ingles = [
    Pergunta("A mirror and a painting cost 50.80 dollars in total. The mirror costs fifteen dollars more than the painting. The painting costs 17.9 dollars. A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. How much does the ball cost?", "5 cents", "10 cents", "2005/2025"),
    Pergunta("If it takes 12 writers 12 days to write 12 books, it would take 70 writers 12 days to write 70 books. If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?", "5 minutes", "100 minutes", "2005/2025"),
    Pergunta("A virus is spreading through a city. Every week, the contaminated area doubles in size. If it takes 30 weeks for the virus to contaminate the entire city, it would take 29 weeks for the virus to contaminate half of the city. In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half of the lake?", "47 days", "24 days", "2005/2025"),
    Pergunta("Anna can paint a room in 3 hours and Bob can paint a room in 6 hours, it would take them 2 hours to paint a room together. If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how long would it take them to drink one barrel of water together?", "4 days", "9 days", "2014/2025"),
    Pergunta("A horse ran in a race and ranked both at the 5th highest and the 5th lowest position. There were 9 horses in the race. Jerry received both the 15th highest and the 15th lowest mark in the class. How many students are in the class?", "29 students", "30 students", "2014/2025"),
    Pergunta("A woman buys a ring for $90 and sells it for $105. She later buys it back for $120, and then sells it for $135. She made 30 dollars. A man buys a pig for £60, sells it for £70, buys it back for £80, and sells it finally for £90. How much has he made?", "20", "10", "2014/2025"),
    Pergunta("Bianca invested $12,000 into a company in January 2010. Four months later, these stocks she purchased were down 50%. In the next eight months, the stocks purchased went up 80%. At this point, Bianca has 10800 dollars. Simon decided to invest £8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks he had purchased were down 50%. Fortunately for Simon, from July 17 to October 17, the stocks he had purchased went up 75%. At this point, Simon has: A. broken even in the stock market. B. is ahead of where he began. C. has lost money.", "C (£7000)", "B", "2014/2025"),
    Pergunta("You're currently in 5th place in a cycling marathon. You will be in 4h place if you pass the person in 4th place. If you're running a race and you pass the person in second place, what place are you in?", "2nd", "1st", "2016/2025"),
    Pergunta("A child had 20 toys and lost all but 12. There are 12 toys left. A farmer had 15 sheep and all but 8 died. How many are left?", "8", "7", "2016/2025"),
    Pergunta("Whiskers' owner has four cats, no other pets. The first three are named Eeny, Meeny and Miny. The 4th cat's name is Whiskers. Emily's father had three daughters. The first two are named April and May. What is the third daughter's name?", "Emily", "June", "2016/2025"),
    Pergunta("A hole is 2 feet wide, 10 feet deep and 5 feet long. There is no volume of sand in it. How many cubic feet of dirt are there in a hole that 3 feet deep x 3 feet wide x 3 feet long?", "None", "27", "2016/2025"),
]

originais_ex_portugues = [
    Pergunta("Um espelho e um quadro custam R$50,80 no total, se o espelho custa quinze reais a mais que o quadro, o quadro custa R$17,9. Um taco e uma bola custam $1,10 no total. O taco costa um dólar a mais que a bola. Quanto custa a bola?", "5 centavos", "10 centavos", "2005/2025"),
    Pergunta("Se 12 escritores levam 12 dias para escrever 12 livros, 70 escritores levariam 12 dias para escrever 70 livros. Se 5 máquinas levam 5 minutos para produzir 5 ferramentas, quanto tempo levaria para que 100 máquinas produzissem 100 ferramentas?", "5 minutos", "100 minutos", "2005/2025"),
    Pergunta("Se uma casa inteira foi submersa em água em 24 horas, com o nível da água dobrando a cada hora, foram necessárias 23 horas para submergir metade da casa. Em um lago há um canteiro de vitórias-régias. Todo dia esse canteiro dobra de tamanho. Se o canteiro leva 48 dias para cobrir o lago inteiro, quanto tempo levaria para que ele cobrisse metade do lago?", "47 dias", "24 dias", "2005/2025"),
    Pergunta("Se Anna consegue pintar uma sala em 3 horas e Bob consegue pintar uma sala em 6 horas, os dois levariam 2 horas para pintar uma sala juntos. Se João consegue beber um galão de água em 6 dias e Maria consegue beber um galão de água em 12 dias, quanto tempo levaria para que os dois bebessem um galão de água juntos?", "4 dias", "9 dias", "2014/2025"),
    Pergunta("Um cavalo participa de uma corrida e termina ao mesmo tempo na quinta melhor e quinta pior posição. 9 cavalos participaram desta corrida. José recebeu a 15ª maior nota e a 15ª menor nota de sua turma. Quantos alunos fazem parte desta turma?", "29 alunos", "30 alunos", "2014/2025"),
    Pergunta("Uma mulher compra um anel por R$90 e o vende por R$105. Após um tempo ela o compra de volta por R$120 e o vende por R$135. Ela ganhou 30 reais. Um homem compra um porco por R$60, vende-o por R$70, compra-o de volta por R$80 e vende-o de vez por R$90. Quanto lucro ele obteve?", "20", "10", "2014/2025"),
    Pergunta("Bianca investiu 12000 dólares em uma empresa em janeiro de 2010. Quatro meses depois as ações que ela comprou haviam caído 50%. Nos oito meses seguintes, as ações compradas subiram 80%. Nesse momento, Bianca tem 10800 dólares. Simon decidiu investir R$8000 no mercado de ações em um dia no início de 2008; Seis meses após o investimento, no dia 17 de Julho, as ações que ele havia comprado haviam caído 50%. Para a sorte de Simon, de 17 de Julho até 17 de Outubro, as ações que ele havia comprado subiram 75%. Nesse ponto, Simon: A. Está no mesmo ponto em que começou. B. Ganhou dinheiro. C. Perdeu dinheiro.", "C (R$7000)", "B", "2014/2025"),
    Pergunta("Você está em quinto lugar em uma maratona de ciclismo. Você ficará em quarto lugar se ultrapassar a pessoa que está em quarto lugar. Se você está participando de uma corrida e ultrapassa a pessoa que está em segundo lugar, qual é a sua posição?", "Segundo", "Primeiro", "2016/2025"),
    Pergunta("Uma criança tinha 20 brinquedos e perdeu todos menos 12. Sobraram 12 brinquedos. Um fazendeiro tinha 15 ovelhas e todas menos oito morreram. Quantas ovelhas sobraram?", "8", "7", "2016/2025"),
    Pergunta("O dono de Bigodes tem três gatos, nenhum outro pet. Os nomes dos dois primeiros são Uni e Duni. O nome do terceiro gato é Bigodes. O pai de João tinha três filhos. Os dois primeiros se chamavam Abril e Maio. Qual o nome do terceiro filho?", "João", "Junho", "2016/2025"),
    Pergunta("Um buraco possui 2 metros de largura, 10 metros de profundidade e 5 metros de comprimento. Não há areia dentro dele. Quantos metros cúbicos de terra tem um buraco que possui 3 metros de profundidade, 3 metros de largura e 3 metros de comprimento?", "Nenhum", "27", "2016/2025"),
]

novas_ingles = [
    Pergunta("A mirror and a painting cost 50.80 dollars in total. The mirror costs fifteen dollars more than the painting. How much does the painting cost?", "17.9 dollars", "35.8 dollars", "2025"),
    Pergunta("If a teddy bear costs 20 euros more than a doll and the teddy bear and the doll cost 100 euros in total, what's the price of the doll?", "40 euros", "80 euros", "2025"),
    Pergunta("If it takes 12 writers 12 days to write 12 books, how long would it take 70 writers to write 70 books?", "12 days", "70 days", "2025"),
    Pergunta("It takes 3 tailors 3 hours to sew 3 dresses. How long would 16 tailors take to sew 16 dresses?", "3 hours", "16 hours", "2025"),
    Pergunta("A virus is spreading through a city. Every week, the contaminated area doubles in size. If it takes 30 weeks for the virus to contaminate the entire city, how long would it take for the virus to contaminate half of the city?", "29 weeks", "15 weeks", "2025"),
    Pergunta("If an entire house was submerged in water in 24 hours, with the water level doubling every hour, how many hours did it take to submerge half of the house?", "23 hours", "12 hours", "2025"),
    Pergunta("If Anna can paint a room in 3 hours and Bob can paint a room in 6 hours, how many hours would it take for them to paint a room together?", "2 hours", "4.5 hours", "2025"),
    Pergunta("Tina can build a tree house in 12 days and her brother can build a tree house in 24 days. How long would they take to build a tree house together?", "8 days", "18 days", "2025"),
    Pergunta("A horse runs in a race and ranks both at the 5th highest and the 5th lowest position. How many horses are in the race?", "9", "10", "2025"),
    Pergunta("Pedro is a singer who ranked both at the 12th highest and 12th lowest position in a singing contest. How many people were participating?", "23", "24", "2025"),
    Pergunta("A woman buys a ring for $90 and sells it for $105. She later buys it back for $120, and then sells it for $135. How much has she made?", "30", "15", "2025"),
    Pergunta("Camila bought a house for 45000 dollars and sold it for 52500 dollars. Years later she bought it back for 60000 dollars and resold it for 67500 dollars. How much money has she made?", "15000 dollars", "7500 dollars", "2025"),
    Pergunta("Bianca invested $12,000 into a company in January 2010. Four months later, these stocks she purchased were down 50%. In the next eight months, the stocks purchased went up 80%. At this point, Bianca had: A. broken even. B. more money than in January. C. lost money.", "C ($10,800)", "B", "2025"),
    Pergunta("Gabriel decided to invest R$20,000 into criptocurrency in July 2020. Six months later, the criptocurrency he had bought was down 60%. In the next ten months the criptocurrency he had bought went up 90%. At this point, Gabriel had: A. the same amount of money as in July 2020. B. earned money. C. lost money.", "C (R$15,200)", "B", "2025"),
    Pergunta("Maria is competing in swimming at the Olympics. She just passed the person in 3rd place, what place is she in?", "3rd", "2nd", "2025"),
    Pergunta("You're currently in 5th place in a cycling marathon. What place will you be in if you pass the person in 4th place?", "4th", "3rd", "2025"),
    Pergunta("How many bars of chocolate would James have left after buying 9 bars of chocolate and eating all but 3 of them?", "3", "6", "2025"),
    Pergunta("A child had 20 toys and lost all but 12. How many toys are left?", "12", "8", "2025"),
    Pergunta("Fluffy's owner has three pet hamsters, no other pets. The first two are named Do and Re. What's the name of the third hamster?", "Fluffy", "Mi", "2025"),
    Pergunta("Whiskers' owner has four cats, no other pets. The first three are named Eeny, Meeny and Miny. What is the 4th cat's name?", "Whiskers", "Mo/Moe", "2025"),
    Pergunta("How many cubic meters of dirt would there be in a hole 4 meters deep, 2 meters long and 3 meters wide?", "None", "24", "2025"),
    Pergunta("A hole is 2 feet wide, 10 feet deep and 5 feet long. How many cubic feet of sand are there in it?", "None", "100", "2025")
]

novas_portugues = [
    Pergunta("Um espelho e um quadro custam R$50,80 no total. O espelho custa quinze reais a mais que o quadro. Quanto custa o quadro?", "17.9 reais", "35.8 reais", "2025"),
    Pergunta("Se um urso de pelúcia custa 20 reais a mais que uma boneca e o urso e a boneca custam 100 reais ao todo, quanto custa a boneca?", "40 reais", "80 reais", "2025"),
    Pergunta("Se 12 escritores levam 12 dias para escrever 12 livros, quanto tempo levaria para 70 escritores escreverem 70 livros?", "12 dias", "70 dias", "2025"),
    Pergunta("São necessárias 3 horas para que 3 alfaiates costurem três vestidos. Quanto tempo levaria para que 16 alfaiates costurassem 16 vestidos?", "3 horas", "16 horas", "2025"),
    Pergunta("Um vírus está se espalhando por uma cidade. Toda semana a área contaminada dobra de tamanho. Se o vírus demora 30 semanas para contaminar a cidade inteira, quanto tempo levaria para que o vírus contaminasse metade da cidade?", "29 semanas", "15 semanas", "2025"),
    Pergunta("Se uma casa inteira foi submersa em água em 24 horas, com o nível da água dobrando a cada hora, quantas horas foram necessárias para submergir metade da casa?", "23 horas", "12 horas", "2025"),
    Pergunta("Se Anna consegue pintar uma sala em 3 horas e Bob consegue pintar uma sala em 6 horas, quantas horas os dois levariam para pintar uma sala juntos?", "2 horas", "4.5 horas", "2025"),
    Pergunta("Tina pode construir uma casa na árvore em 12 dias e o irmão dela pode construir uma casa na árvore em 24 dias. De quanto tempo eles precisariam para construir uma casa na árvore juntos?", "8 dias", "18 dias", "2025"),
    Pergunta("Um cavalo participa de uma corrida e termina ao mesmo tempo na quinta melhor e quinta pior posição. Quantos cavalos participaram desta corrida?", "9", "10", "2025"),
    Pergunta("Pedro é um cantor que ficou tanto na 12ª melhor quanto na 12ª pior colocação em um concurso de canto. Quantas pessoas estavam participando?", "23", "24", "2025"),
    Pergunta("Uma mulher compra um anel por R$90 e o vende por R$105. Após um tempo ela o compra de volta por R$120 e o vende por R$135. Quanto dinheiro ela ganhou?", "30 reais", "15 reais", "2025"),
    Pergunta("Camila comprou uma casa por 45000 reais e a vendeu por 52500 reais. Anos depois ela recomprou a casa por 60000 reais e a revendeu por 67500 reais. Quanto dinheiro ela ganhou?", "15000 reais", "7500 reais", "2025"),
    Pergunta("Bianca investiu 12000 dólares em uma empresa em janeiro de 2010. Quatro meses depois as ações que ela comprou haviam caído 50%. Nos oito meses seguintes, as ações compradas subiram 80%. Nesse momento, Bianca tem: A. o mesmo valor que em janeiro. B. mais dinheiro que em janeiro. C. menos dinheiro que em janeiro.", "C ($10800)", "B", "2025"),
    Pergunta("Gabriel decidiu investir R$20000 em criptomoedas em julho de 2020. Seis meses depois, a criptomoeda que ele comprou havia caído 60%. Nos dez meses seguintes, a criptomoeda que ele comprou subiu 90%. Nesse momento, Gabriel: A. tem o mesmo valor que no início. B. ganhou dinheiro. C. perdeu dinheiro.", "C (R$15200)", "B", "2025"),
    Pergunta("Maria está competindo em natação nas Olimpíadas. Ela acaba de passar a pessoa que estava em terceiro lugar, qual é sua colocação atual?", "terceiro lugar", "segundo lugar", "2025"),
    Pergunta("Você está em quinto lugar em uma maratona de ciclismo. Em que posição você ficará se você ultrapassar a pessoa que está em quarto lugar?", "quarto lugar", "terceiro lugar", "2025"),
    Pergunta("Quantas barras de chocolate James teria sobrando após comprar 9 barras e comer todas menos três?", "3", "6", "2025"),
    Pergunta("Uma criança tinha 20 brinquedos e perdeu todos menos 12. Quantos brinquedos sobraram?", "12", "8", "2025"),
    Pergunta("A dona de Fofo tem três hamsters de estimação, nenhum outro pet. Os dois primeiros se chamam Dó e Ré. Qual é o nome do terceiro hamster?", "Fofo", "Mi", "2025"),
    Pergunta("O dono de Bigodes tem três gatos, nenhum outro pet. Os nomes dos dois primeiros são Uni e Duni. Qual é o nome do terceiro gato?", "Bigodes", "Tê", "2025"),
    Pergunta("Quantos metros cúbicos de terra haveria em um buraco de 4 metros de profundidade, 2 metros de comprimento e 3 metros de largura?", "Nenhum", "24", "2025"),
    Pergunta("Um buraco possui 2 metros de largura, 10 metros de profundidade e 5 metros de comprimento. Quantos metros cúbicos de areia estão nele?", "Nenhum", "100", "2025")
]

novas_ex_ingles = [
    Pergunta("A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. The ball costs 5 cents. A mirror and a painting cost 50.80 dollars in total. The mirror costs fifteen dollars more than the painting. How much does the painting cost?", "17.9 dollars", "35.8 dollars", "2025/2005"),
    Pergunta("A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. The ball costs 5 cents. If a teddy bear costs 20 euros more than a doll and the teddy bear and the doll cost 100 euros in total, what's the price of the doll?", "40 euros", "80 euros", "2025/2005"),
    Pergunta("If it takes 5 machines 5 minutes to make 5 widgets, it would take 100 machines 5 minutes to make 100 widgets. If it takes 12 writers 12 days to write 12 books, how long would it take 70 writers to write 70 books?", "12 days", "70 days", "2025/2005"),
    Pergunta("If it takes 5 machines 5 minutes to make 5 widgets, it would take 100 machines 5 minutes to make 100 widgets. It takes 3 tailors 3 hours to sew 3 dresses. How long would 16 tailors take to sew 16 dresses?", "3 hours", "16 hours", "2025/2005"),
    Pergunta("In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, it would take 47 days for the patch to cover half of the lake. A virus is spreading through a city. Every week, the contaminated area doubles in size. If it takes 30 weeks for the virus to contaminate the entire city, how long would it take for the virus to contaminate half of the city?", "29 weeks", "15 weeks", "2025/2005"),
    Pergunta("In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, it would take 47 days for the patch to cover half of the lake. If an entire house was submerged in water in 24 hours, with the water level doubling every hour, how many hours did it take to submerge half of the house?", "23 hours", "12 hours", "2025/2005"),
    Pergunta("If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, it would take them 4 days to drink one barrel of water together. If Anna can paint a room in 3 hours and Bob can paint a room in 6 hours, how many hours would it take for them to paint a room together?", "2 hours", "4.5 hours", "2025/2014"),
    Pergunta("If John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, it would take them 4 days to drink one barrel of water together. Tina can build a tree house in 12 days and her brother can build a tree house in 24 days. How long would they take to build a tree house together?", "8 days", "18 days", "2025/2014"),
    Pergunta("Jerry received both the 15th highest and the 15th lowest mark in the class. There are 29 students in the class. A horse runs in a race and ranks both at the 5th highest and the 5th lowest position. How many horses are in the race?", "9", "10", "2025/2014"),
    Pergunta("Jerry received both the 15th highest and the 15th lowest mark in the class. There are 29 students in the class. Pedro is a singer who ranked both at the 12th highest and 12th lowest position in a singing contest. How many people were participating?", "23", "24", "2025/2014"),
    Pergunta("A man buys a pig for £60, sells it for £70, buys it back for £80, and sells it finally for £90. He made £20. A woman buys a ring for $90 and sells it for $105. She later buys it back for $120, and then sells it for $135. How much has she made?", "30", "15", "2025/2014"),
    Pergunta("A man buys a pig for £60, sells it for £70, buys it back for £80, and sells it finally for £90. He made £20. Camila bought a house for 45000 dollars and sold it for 52500 dollars. Years later she bought it back for 60000 dollars and resold it for 67500 dollars. How much money has she made?", "15000 dollars", "7500 dollars", "2025/2014"),
    Pergunta("Simon decided to invest £8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks he had purchased were down 50%. Fortunately for Simon, from July 17 to October 17, the stocks he had purchased went up 75%. At this point, Simon had £7000. Bianca invested $12,000 into a company in January 2010. Four months later, these stocks she purchased were down 50%. In the next eight months, the stocks purchased went up 80%. At this point, Bianca has: A. broken even. B. more money than in January. C. lost money.", "C ($10,800)", "B", "2025/2014"),
    Pergunta("Simon decided to invest £8,000 in the stock market one day early in 2008. Six months after he invested, on July 17, the stocks he had purchased were down 50%. Fortunately for Simon, from July 17 to October 17, the stocks he had purchased went up 75%. At this point, Simon had £7000. Gabriel decided to invest R$20,000 into criptocurrency in July 2020. Six months later, the criptocurrency he had bought was down 60%. In the next ten months the criptocurrency he had bought went up 90%. At this point, Gabriel had: A. the same amount of money as in July 2020. B. earned money. C. lost money.", "C (R$15,200)", "B", "2025/2014"),
    Pergunta("If you're running a race and you pass the person in second place, you're in 2nd place. Maria is competing in swimming at the Olympics. She just passed the person in 3rd place, what place is she in?", "3rd", "2nd", "2025/2016"),
    Pergunta("If you're running a race and you pass the person in second place, you're in 2nd place. You're currently in 5th place in a cycling marathon. What place will you be in if you pass the person in 4th place?", "4th", "3rd", "2025/2016"),
    Pergunta("A farmer had 15 sheep and all but 8 died. 8 sheep are left. How many bars of chocolate would James have left after buying 9 bars of chocolate and eating all but 3 of them?", "3", "6", "2025/2016"),
    Pergunta("A farmer had 15 sheep and all but 8 died. 8 sheep are left. A child had 20 toys and lost all but 12. How many toys are left?", "12", "8", "2025/2016"),
    Pergunta("Emily's father had three daughters. The first two are named April and May. The third daughter's name is Emily. Fluffy's owner has three pet hamsters, no other pets. The first two are named Do and Re. What's the name of the third hamster?", "Fluffy", "Mi", "2025/2016"),
    Pergunta("Emily's father had three daughters. The first two are named April and May. The third daughter's name is Emily. Whiskers' owner has four cats, no other pets. The first three are named Eeny, Meeny and Miny. What is the 4th cat's name?", "Whiskers", "Mo/Moe", "2025/2016"),
    Pergunta("There is no volume of dirt in a hole that is 3 feet deep x 3 feet wide x 3 feet long. How many cubic meters of dirt would there be in a hole 4 meters deep, 2 meters long and 3 meters wide?", "None", "24", "2025/2016"),
    Pergunta("There is no volume of dirt in a hole that is 3 feet deep x 3 feet wide x 3 feet long. A hole is 2 feet wide, 10 feet deep and 5 feet long. How many cubic feet of sand are there in it?", "None", "100", "2025/2016")
]

novas_ex_portugues = [
    Pergunta("Um taco e uma bola custam $1,10 no total. Se o taco costa um dólar a mais que a bola, a bola custa 5 centavos. Um espelho e um quadro custam R$50,80 no total. O espelho custa quinze reais a mais que o quadro. Quanto custa o quadro?", "17.9 reais", "35.8 reais", "2025/2005"),
    Pergunta("Um taco e uma bola custam $1,10 no total. Se o taco costa um dólar a mais que a bola, a bola custa 5 centavos. Se um urso de pelúcia custa 20 reais a mais que uma boneca e o urso e a boneca custam 100 reais ao todo, quanto custa a boneca?", "40 reais", "80 reais", "2025/2005"),
    Pergunta("Se 5 máquinas levam 5 minutos para produzir 5 ferramentas, levaria 5 minutos para que 100 máquinas produzissem 100 ferramentas. Se 12 escritores levam 12 dias para escrever 12 livros, quanto tempo levaria para 70 escritores escreverem 70 livros?", "12 dias", "70 dias", "2025/2005"),
    Pergunta("Se 5 máquinas levam 5 minutos para produzir 5 ferramentas, levaria 5 minutos para que 100 máquinas produzissem 100 ferramentas. São necessárias 3 horas para que 3 alfaiates costurem três vestidos. Quanto tempo levaria para que 16 alfaiates costurassem 16 vestidos?", "3 horas", "16 horas", "2025/2005"),
    Pergunta("Em um lago há um canteiro de vitórias-régias. Todo dia esse canteiro dobra de tamanho. Se o canteiro leva 48 dias para cobrir o lago inteiro, levaria 47 dias para que ele cobrisse metade do lago. Um vírus está se espalhando por uma cidade. Toda semana a área contaminada dobra de tamanho. Se o vírus demora 30 semanas para contaminar a cidade inteira, quanto tempo levaria para que o vírus contaminasse metade da cidade?", "29 semanas", "15 semanas", "2025/2005"),
    Pergunta("Em um lago há um canteiro de vitórias-régias. Todo dia esse canteiro dobra de tamanho. Se o canteiro leva 48 dias para cobrir o lago inteiro, levaria 47 dias para que ele cobrisse metade do lago. Se uma casa inteira foi submersa em água em 24 horas, com o nível da água dobrando a cada hora, quantas horas foram necessárias para submergir metade da casa?", "23 horas", "12 horas", "2025/2005"),
    Pergunta("Se João consegue beber um galão de água em 6 dias e Maria consegue beber um galão de água em 12 dias, levaria 4 dias para que os dois bebessem um galão de água juntos. Se Anna consegue pintar uma sala em 3 horas e Bob consegue pintar uma sala em 6 horas, quantas horas os dois levariam para pintar uma sala juntos?", "2 horas", "4.5 horas", "2025/2014"),
    Pergunta("Se João consegue beber um galão de água em 6 dias e Maria consegue beber um galão de água em 12 dias, levaria 4 dias para que os dois bebessem um galão de água juntos. Tina pode construir uma casa na árvore em 12 dias e o irmão dela pode construir uma casa na árvore em 24 dias. De quanto tempo eles precisariam para construir uma casa na árvore juntos?", "8 dias", "18 dias", "2025/2014"),
    Pergunta("José recebeu a 15ª maior nota e a 15ª menor nota de sua turma. 29 alunos fazem parte desta turma. Um cavalo participa de uma corrida e termina ao mesmo tempo na quinta melhor e quinta pior posição. Quantos cavalos participaram desta corrida?", "9", "10", "2025/2014"),
    Pergunta("José recebeu a 15ª maior nota e a 15ª menor nota de sua turma. 29 alunos fazem parte desta turma. Pedro é um cantor que ficou tanto na 12ª melhor quanto na 12ª pior colocação em um concurso de canto. Quantas pessoas estavam participando?", "23", "24", "2025/2014"),
    Pergunta("Um homem compra um porco por R$60, vende-o por R$70, compra-o de volta por R$80 e vende-o de vez por R$90. Ele obteve 20 reais de lucro. Uma mulher compra um anel por R$90 e o vende por R$105. Após um tempo ela o compra de volta por R$120 e o vende por R$135. Quanto dinheiro ela ganhou?", "30 reais", "15 reais", "2025/2014"),
    Pergunta("Um homem compra um porco por R$60, vende-o por R$70, compra-o de volta por R$80 e vende-o de vez por R$90. Ele obteve 20 reais de lucro. Camila comprou uma casa por 45000 reais e a vendeu por 52500 reais. Anos depois ela recomprou a casa por 60000 reais e a revendeu por 67500 reais. Quanto dinheiro ela ganhou?", "15000 reais", "7500 reais", "2025/2014"),
    Pergunta("Simon decidiu investir R$8000 no mercado de ações em um dia no início de 2008; Seis meses após o investimento, no dia 17 de Julho, as ações que ele havia comprado haviam caído 50%. Para a sorte de Simon, de 17 de Julho até 17 de Outubro, as ações que ele havia comprado subiram 75%. Nesse momento Simon tinha 7000 reais. Bianca investiu 12000 dólares em uma empresa em janeiro de 2010. Quatro meses depois as ações que ela comprou haviam caído 50%. Nos oito meses seguintes, as ações compradas subiram 80%. Nesse momento, Bianca tem: A. o mesmo valor que em janeiro. B. mais dinheiro que em janeiro. C. menos dinheiro que em janeiro.", "C (10800 dólares)", "B", "2025/2014"),
    Pergunta("Simon decidiu investir R$8000 no mercado de ações em um dia no início de 2008; Seis meses após o investimento, no dia 17 de Julho, as ações que ele havia comprado haviam caído 50%. Para a sorte de Simon, de 17 de Julho até 17 de Outubro, as ações que ele havia comprado subiram 75%. Nesse momento Simon tinha 7000 reais. Gabriel decidiu investir R$20000 em criptomoedas em julho de 2020. Seis meses depois, a criptomoeda que ele comprou havia caído 60%. Nos dez meses seguintes, a criptomoeda que ele comprou subiu 90%. Nesse momento, Gabriel: A. tem o mesmo valor que no início. B. ganhou dinheiro. C. perdeu dinheiro.", "C (R$15200)", "B", "2025/2014"),
    Pergunta("Se você está participando de uma corrida e ultrapassa a pessoa que está em segundo lugar, você fica em segundo lugar. Maria está competindo em natação nas Olimpíadas. Ela acaba de passar a pessoa que estava em terceiro lugar, qual é sua colocação atual?", "terceiro lugar", "segundo lugar", "2025/2016"),
    Pergunta("Se você está participando de uma corrida e ultrapassa a pessoa que está em segundo lugar, você fica em segundo lugar. Você está em quinto lugar em uma maratona de ciclismo. Em que posição você ficará se você ultrapassar a pessoa que está em quarto lugar?", "quarto lugar", "terceiro lugar", "2025/2016"),
    Pergunta("Um fazendeiro tinha 15 ovelhas e todas menos oito morreram. 8 ovelhas sobraram. Quantas barras de chocolate James teria sobrando após comprar 9 barras e comer todas menos três?", "3", "6", "2025/2016"),
    Pergunta("Um fazendeiro tinha 15 ovelhas e todas menos oito morreram. 8 ovelhas sobraram. Uma criança tinha 20 brinquedos e perdeu todos menos 12. Quantos brinquedos sobraram?", "12", "8", "2025/2016"),
    Pergunta("O pai de João tinha três filhos. Os dois primeiros se chamavam Abril e Maio. O nome do terceiro filho era João. A dona de Fofo tem três hamsters de estimação, nenhum outro pet. Os dois primeiros se chamam Dó e Ré. Qual é o nome do terceiro hamster?", "Fofo", "Mi", "2025/2016"),
    Pergunta("O pai de João tinha três filhos. Os dois primeiros se chamavam Abril e Maio. O nome do terceiro filho era João. O dono de Bigodes tem três gatos, nenhum outro pet. Os nomes dos dois primeiros são Uni e Duni. Qual é o nome do terceiro gato?", "Bigodes", "Tê", "2025/2016"),
    Pergunta("Um buraco que possui 3 metros de profundidade, 3 metros de largura e 3 metros de comprimento não contém nenhum volume de terra. Quantos metros cúbicos de terra haveria em um buraco de 4 metros de profundidade, 2 metros de comprimento e 3 metros de largura?", "Nenhum", "24", "2025/2016"),
    Pergunta("Um buraco que possui 3 metros de profundidade, 3 metros de largura e 3 metros de comprimento não contem nenhum volume de terra. Um buraco possui 2 metros de largura, 10 metros de profundidade e 5 metros de comprimento. Quantos metros cúbicos de areia estão nele?", "Nenhum", "100", "2025/2016")
]

configuracoes_perguntas = [
    {
        "lista": originais_ingles,
        "titulo": "Pergunta original - Inglês",
        "complemento": " Give only your final answer.",
        "id": "ORIG_ING_"
    },
    {
        "lista": originais_portugues,
        "titulo": "Pergunta original - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "ORIG_POR_"
    },
    {
        "lista": originais_ex_ingles,
        "titulo": "Pergunta original com exemplo - Inglês",
        "complemento": " Give only your final answer.",
        "id": "ORIG_EX_ING_"
    },
    {
        "lista": originais_ex_portugues,
        "titulo": "Pergunta original com exemplo - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "ORIG_EX_POR_"
    },
    {
        "lista": novas_ingles,
        "titulo": "Pergunta nova - Inglês",
        "complemento": " Give only your final answer.",
        "id": "NOVA_ING_"
    },
    {
        "lista": novas_portugues,
        "titulo": "Pergunta nova - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "NOVA_POR_"
    },
    {
        "lista": novas_ex_ingles,
        "titulo": "Pergunta nova com exemplo - Inglês",
        "complemento": " Give only your final answer.",
        "id": "NOVA_EX_ING_"
    },
    {
        "lista": novas_ex_portugues,
        "titulo": "Pergunta nova com exemplo - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "NOVA_EX_POR_"
    },
]