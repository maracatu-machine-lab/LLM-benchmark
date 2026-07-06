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

originais_espanhol = [
    Pergunta("Un bate y una pelota cuestan $1.10 en total. El bate cuesta un dólar más que la pelota. ¿Cuánto cuesta la pelota?", "5 centavos", "10 centavos", "2005"),
    Pergunta("Si 5 máquinas tardan 5 minutos en hacer 5 objetos, ¿cuánto tiempo tardarían 100 máquinas en hacer 100 objetos?", "5 minutos", "100 minutos", "2005"),
    Pergunta("En un lago hay un grupo de nenúfares. Cada día, el grupo dobla su tamaño. Si tarda 48 días en cubrir todo el lago, ¿cuánto tiempo tardaría en cubrir la mitad?", "47 días", "24 días", "2005"),
    Pergunta("Si Juan puede beber un barril de agua en 6 días y María puede beber un barril en 12 días, ¿cuánto tiempo tardarían en beber un barril juntos?", "4 días", "9 días", "2014"),
    Pergunta("Jerry recibió tanto la 15ª calificación más alta como la 15ª más baja de la clase. ¿Cuántos estudiantes hay en la clase?", "29 estudiantes", "30 estudiantes", "2014"),
    Pergunta("Un hombre compra un cerdo por £60, lo vende por £70, lo vuelve a comprar por £80 y lo vende finalmente por £90. ¿Cuánto dinero ganó?", "20", "10", "2014"),
    Pergunta("Simón decidió invertir £8,000 en la bolsa a principios de 2008. Seis meses después, el 17 de julio, sus acciones habían bajado un 50%. Afortunadamente, del 17 de julio al 17 de octubre, las acciones subieron un 75%. En este punto, Simón: A. quedó igual. B. está mejor que al principio. C. perdió dinero.", "C (£7000)", "B", "2014"),
    Pergunta("Si estás en una carrera y adelantas a la persona que va en segundo lugar, ¿en qué lugar estás?", "2.º", "1.º", "2016"),
    Pergunta("Un granjero tenía 15 ovejas y murieron todas menos 8. ¿Cuántas quedan?", "8", "7", "2016"),
    Pergunta("El padre de Emily tenía tres hijas. Las dos primeras se llaman Abril y Mayo. ¿Cómo se llama la tercera hija?", "Emily", "Junio", "2016"),
    Pergunta("¿Cuántos pies cúbicos de tierra hay en un hoyo de 3 pies de profundidad x 3 pies de ancho x 3 pies de largo?", "Nada", "27", "2016"),
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
    Pergunta("A hole is 2 feet wide, 10 feet deep and 5 feet long. How many cubic feet of sand are there in it?", "None", "100", "2025"),
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
    Pergunta("Um buraco possui 2 metros de largura, 10 metros de profundidade e 5 metros de comprimento. Quantos metros cúbicos de areia estão nele?", "Nenhum", "100", "2025"),
]

novas_espanhol = [
    Pergunta("Un espejo y un cuadro cuestan $50.80 en total. El espejo cuesta quince dólares más que el cuadro. ¿Cuánto cuesta el cuadro?", "17.9 dólares", "35.8 dólares", "2025"),
    Pergunta("Si un oso de peluche cuesta 20 euros más que una muñeca y el oso de peluche y la muñeca cuestan 100 euros en total, ¿cuál es el precio de la muñeca?", "40 euros", "80 euros", "2025"),
    Pergunta("Si 12 escritores tardan 12 días en escribir 12 libros, ¿cuánto tiempo tardarían 70 escritores en escribir 70 libros?", "12 días", "70 días", "2025"),
    Pergunta("Tres sastres tardan 3 horas en coser 3 vestidos. ¿Cuánto tiempo les tomaría a 16 sastres coser 16 vestidos?", "3 horas", "16 horas", "2025"),
    Pergunta("Un virus se está propagando por una ciudad. Cada semana, el área contaminada dobla su tamaño. Si el virus tarda 30 semanas en contaminar toda la ciudad, ¿cuánto tiempo tardaría en contaminar la mitad?", "29 semanas", "15 semanas", "2025"),
    Pergunta("Si una casa entera quedó sumergida bajo el agua en 24 horas, y el nivel del agua se duplicaba cada hora, ¿cuántas horas tardó en sumergirse la mitad de la casa?", "23 horas", "12 horas", "2025"),
    Pergunta("Si Anna puede pintar una habitación en 3 horas y Bob puede pintar una habitación en 6 horas, ¿cuántas horas tardarían en pintar una habitación juntos?", "2 horas", "4.5 horas", "2025"),
    Pergunta("Tina puede construir una casa en un árbol en 12 días y su hermano puede construirla en 24 días. ¿Cuánto tiempo tardarían en construir una casa en un árbol juntos?", "8 días", "18 días", "2025"),
    Pergunta("Un caballo corre en una carrera y queda tanto en la 5.ª posición más alta como en la 5.ª más baja. ¿Cuántos caballos hay en la carrera?", "9", "10", "2025"),
    Pergunta("Pedro es un cantante que quedó tanto en la 12.ª posición más alta como en la 12.ª más baja en un concurso de canto. ¿Cuántas personas participaron?", "23", "24", "2025"),
    Pergunta("Una mujer compra un anillo por $90 y lo vende por $105. Luego lo vuelve a comprar por $120 y después lo vende por $135. ¿Cuánto dinero ganó?", "30", "15", "2025"),
    Pergunta("Camila compró una casa por 45,000 dólares y la vendió por 52,500 dólares. Años después la volvió a comprar por 60,000 dólares y la revendió por 67,500 dólares. ¿Cuánto dinero ganó?", "15,000 dólares", "7,500 dólares", "2025"),
    Pergunta("Bianca invirtió $12,000 en una empresa en enero de 2010. Cuatro meses después, las acciones que compró bajaron un 50%. En los siguientes ocho meses, las acciones subieron un 80%. En este punto, Bianca: A. recuperó su inversión. B. tiene más dinero que en enero. C. perdió dinero.", "C ($10,800)", "B", "2025"),
    Pergunta("Gabriel decidió invertir R$20,000 en criptomonedas en julio de 2020. Seis meses después, las criptomonedas que compró bajaron un 60%. En los siguientes diez meses, las criptomonedas subieron un 90%. En este punto, Gabriel: A. tiene la misma cantidad de dinero que en julio de 2020. B. ganó dinero. C. perdió dinero.", "C (R$15,200)", "B", "2025"),
    Pergunta("María está compitiendo en natación en los Juegos Olímpicos. Acaba de adelantar a la persona que iba en 3.er lugar, ¿en qué lugar está?", "3.er", "2.º", "2025"),
    Pergunta("Actualmente estás en el 5.º lugar de un maratón de ciclismo. ¿En qué lugar estarás si adelantas a la persona que va en 4.º lugar?", "4.º", "3.er", "2025"),
    Pergunta("¿Cuántas barras de chocolate le quedarían a James después de comprar 9 barras y comerse todas menos 3?", "3", "6", "2025"),
    Pergunta("Un niño tenía 20 juguetes y los perdió todos menos 12. ¿Cuántos juguetes le quedan?", "12", "8", "2025"),
    Pergunta("El dueño de Fluffy tiene tres hámsteres como mascotas, no tiene otras mascotas. Los dos primeros se llaman Do y Re. ¿Cómo se llama el tercer hámster?", "Fluffy", "Mi", "2025"),
    Pergunta("El dueño de Whiskers tiene cuatro gatos, no tiene otras mascotas. Los tres primeros se llaman Eeny, Meeny y Miny. ¿Cómo se llama el cuarto gato?", "Whiskers", "Mo/Moe", "2025"),
    Pergunta("¿Cuántos metros cúbicos de tierra habría en un hoyo de 4 metros de profundidad, 2 metros de largo y 3 metros de ancho?", "Nada", "24", "2025"),
    Pergunta("Un hoyo tiene 2 pies de ancho, 10 pies de profundidad y 5 pies de largo. ¿Cuántos pies cúbicos de arena hay en él?", "Nada", "100", "2025"),
]

originais_ruidos_ingles = [
    Pergunta("During Christmas, a premium bat was sold for $2.00, and the price difference between that bat and a ball reached $1.10. Meanwhile, at the local sports shop, a standard bat and a ball cost $1.10 in total. The standard bat costs $1.00 more than the ball. How much does the standard ball cost? Knowing this, consider also that on Black Friday, the premium bat appeared for $1.50 and the difference between bat and ball was $0.90, and that at the store across the street, a similar ball costs $0.40.", "5 cents", "10 cents", "2005"),
    Pergunta("At the competitor factory, 5 machines take 10 minutes to operate, with a production-to-time multiplier of 2x. However, in the main plant, if it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 of these machines to make 100 widgets? Also consider that during the night shift, the quantity produced was 50 widgets, and that with the old model, 100 machines operated for 120 minutes, creating a difference of 110 minutes compared to the operational time of 5 machines.", "5 minutes", "100 minutes", "2005"),
    Pergunta("In the North Lake, the initial size of the patch was 5sqm, with a growth rate that reached triple that of the South Lake during the summer. Meanwhile, in East Lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire East Lake, how long would it take for the patch to cover half of it? For comparison, it is known that in the South Lake, total coverage took 30 days and half coverage took 15 days, resulting in a difference of 15 days between the two marks.", "47 days", "24 days", "2005"),
    Pergunta("At the summer camp, John's speed to finish a barrel was 4 days, making the difference between Mary's speed and his speed exactly 4 days. However, at the Base Camp, if John can drink one barrel of water in 6 days, and Mary can drink one barrel of water in 12 days, how long would it take them to drink one barrel of water together? Keep in mind that at the winter camp, Mary's speed was 8 days, making the ratio of Mary's speed to John's speed 2x, and that last year they drank a total of 3 barrels.", "4 days", "9 days", "2014"),
    Pergunta("On the math test, Jerry's highest mark rank was 10th and his lowest mark rank was also 10th, meaning the sum of his highest and lowest ranks was 20. By contrast, in his history class, Jerry received both the 15th highest and the 15th lowest mark. How many students are in the history class? Additionally, note that in the physics class there were 45 total students, and the difference in the number of students between physics and math last semester was 26.", "29 students", "30 students", "2014"),
    Pergunta("At the local market, the first buy of a pig was £50 and the first sell was £55, yielding a profit between the first sell and buy of £5. However, at the annual livestock auction, a man buys a pig for £60, sells it for £70, buys it back for £80, and sells it finally for £90. How much has he made from these specific trades? Consider also that at the county fair his total profit was £15, and the difference between the county fair profit and the local market profit last month was £10.", "20", "10", "2014"),
    Pergunta("In the year 2007, an initial investment of £10,000 saw a ratio of initial investment to final value of 1.5 after an unpredictable market cycle where the difference between the recovery and the drop was 20%. Meanwhile, Simon decided to invest £8,000 in the TechFund one day early in 2008. Six months after he invested, on July 17, the TechFund stocks he had purchased were down 50%. Fortunately for Simon, from July 17 to October 17, the TechFund stocks he had purchased went up 75%. At this point, Simon has: A. broken even in the TechFund. B. is ahead of where he began. C. has lost money. Keep in mind that during the August crash the drop percentage was 40% and the subsequent November rally brought a recovery percentage of 60%.", "C (£7000)", "B", "2014"),
    Pergunta("In the city marathon, out of 50 total runners, the difference between the total runners and your current position was 47. However, if you're running the State Championship 5K and you pass the person in second place, what place are you in? Remember that in the sprint event, passing the person in 3rd position meant your current position was 3rd, resulting in a rank change of 0 relative to the person you just overtook.", "2nd", "1st", "2016"),
    Pergunta("At the neighboring farm, there were 20 initial cows and 10 died cows, meaning the difference between initial cows and died cows was 10. Meanwhile, at Valley Farm, a farmer had 15 sheep and all but 8 died. How many sheep are left at Valley Farm? Consider as well that during the winter storm, the number of surviving pigs was 5, creating a ratio of surviving pigs to died cows of exactly 0.5.", "8", "7", "2016"),
    Pergunta("Uncle Bob had 2 total sons, where the first son's birth month was June and the second son's birth month was July, meaning the difference between their birth months is 1 month. On the other hand, in Emily's immediate household, her father had three daughters. The first two are named April and May. What is the third daughter's name? Furthermore, looking at the entire family tree, the sum of all daughters and sons equals 5.", "Emily", "June", "2016"),
    Pergunta("For the backyard project, a hole with a depth of 5 feet and a width of 2 feet generated a total volume of 50 cubic feet. However, how many cubic feet of dirt are there in a hole at the construction site that is 3 feet deep x 3 feet wide x 3 feet long? Note that in the front yard, the total dirt removed was 10 cubic feet, and during the summer work, the difference between the backyard depth and the front yard depth was exactly 2 feet.", "None", "27", "2016"),
]
originais_ruidos_portugues = [
    Pergunta("Durante o Natal, um taco premium foi vendido por $2,00, e a diferença de preço entre esse taco e uma bola chegou a $1,10. Enquanto isso, na loja de esportes local, um taco e uma bola padrão custam $1,10 no total. O taco padrão custa um dólar a mais que a bola. Quanto custa a bola padrão? Sabendo disso, considere também que na Black Friday, o taco premium apareceu por $1,50 e a diferença entre taco e bola foi de $0,90, e que na loja da frente, uma bola semelhante custa $0,40.", "5 centavos", "10 centavos", "2005"),
    Pergunta("Na fábrica concorrente, 5 máquinas levam 10 minutos para operar, com um multiplicador de produção em relação ao tempo de 2x. No entanto, na fábrica principal, se 5 máquinas levam 5 minutos para produzir 5 ferramentas, quanto tempo levaria para que 100 dessas máquinas produzissem 100 ferramentas? Considere também que durante o turno da noite, a quantidade produzida foi de 50 ferramentas, e que com o modelo antigo, 100 máquinas operaram por 120 minutos, criando uma diferença de 110 minutos em relação ao tempo operacional de 5 máquinas.", "5 minutos", "100 minutos", "2005"),
    Pergunta("No lago Norte, o tamanho inicial do canteiro era de 5m², com uma taxa de crescimento que chegou a ser o triplo da do lago Sul durante o verão. Enquanto isso, no lago Leste, há um canteiro de vitórias-régias. Todo dia esse canteiro dobra de tamanho. Se o canteiro leva 48 dias para cobrir o lago Leste inteiro, quanto tempo levaria para que ele cobrisse metade do lago? Para fins de comparação, sabe-se ainda que no lago Sul, a cobertura total levou 30 dias e a da metade levou 15 dias, resultando em uma diferença de 15 dias entre as duas marcas.", "47 dias", "24 dias", "2005"),
    Pergunta("No acampamento de verão, o tempo de João para terminar um galão era de 4 dias, fazendo com que a diferença entre o tempo de Maria e o dele fosse exatamente 4 dias. No entanto, no acampamento base, se João consegue beber um galão de água em 6 dias e Maria consegue beber um galão de água em 12 dias, quanto tempo levaria para que os dois bebessem um galão de água juntos? Tenha em mente que no acampamento de inverno, o tempo de Maria foi de 8 dias, fazendo com que a proporção do tempo de Maria para o de João fosse de 2x, e que no ano passado eles beberam um total de 3 galões.", "4 dias", "9 dias", "2014"),
    Pergunta("Na prova de matemática, a classificação mais alta de José foi o 10º lugar e a sua classificação mais baixa também foi o 10º, o que significa que a soma das suas classificações mais alta e mais baixa foi 20. Em contrapartida, na sua turma de história, José recebeu a 15ª maior nota e a 15ª menor nota. Quantos alunos fazem parte desta turma de história? Além disso, note que na turma de física havia 45 alunos no total, e a diferença no número de alunos entre física e matemática no semestre passado foi de 26.", "29 alunos", "30 alunos", "2014"),
    Pergunta("No mercado local, a primeira compra de um porco foi por R$50 e a primeira venda por R$55, rendendo um lucro de R$5 entre a primeira venda e a compra. No entanto, no leilão anual de gado, um homem compra um porco por R$60, vende-o por R$70, compra-o de volta por R$80, e vende-o de vez por R$90. Quanto lucro ele obteve nessas negociações específicas? Considere também que na feira municipal seu lucro total foi de R$15, e a diferença entre o lucro da feira municipal e o lucro do mercado local no mês passado foi de R$10.", "20", "10", "2014"),
    Pergunta("No ano de 2007, um investimento inicial de R$10.000 viu uma proporção do investimento inicial para o valor final de 1,5 após um ciclo de mercado imprevisível, onde a diferença entre a recuperação e a queda foi de 20%. Enquanto isso, Simon decidiu investir R$8000 no Fundo de Tecnologia em um dia no início de 2008; Seis meses após o investimento, no dia 17 de Julho, as ações do fundo que ele havia comprado haviam caído 50%. Para a sorte de Simon, de 17 de Julho até 17 de Outubro, as ações que ele havia comprado subiram 75%. Nesse ponto, Simon: A. Está no mesmo ponto em que começou no fundo. B. Ganhou dinheiro. C. Perdeu dinheiro. Tenha em mente que durante a queda de agosto a porcentagem de queda foi de 40% e a subsequente recuperação de novembro trouxe uma porcentagem de recuperação de 60%.", "C (R$7000)", "B", "2014"),
    Pergunta("Na maratona da cidade, de um total de 50 corredores, a diferença entre o total de corredores e a sua posição atual era de 47. No entanto, se você está participando do Campeonato Estadual de 5K e ultrapassa a pessoa que está em segundo lugar, qual é a sua posição? Lembre-se que na prova de velocidade, ultrapassar a pessoa na 3ª posição significava que sua posição atual era a 3ª, resultando em uma mudança de classificação de 0 em relação à pessoa que você acabou de ultrapassar.", "Segundo", "Primeiro", "2016"),
    Pergunta("Na fazenda vizinha, havia 20 vacas inicialmente e 10 vacas morreram, o que significa que a diferença entre as vacas iniciais e as vacas mortas foi de 10. Enquanto isso, na Fazenda do Vale, um fazendeiro tinha 15 ovelhas e todas menos oito morreram. Quantas ovelhas sobraram na Fazenda do Vale? Considere também que durante a tempestade de inverno, o número de porcos sobreviventes foi 5, criando uma proporção de porcos sobreviventes para vacas mortas de exatamente 0,5.", "8", "7", "2016"),
    Pergunta("O tio Beto teve 2 filhos no total, onde o mês de nascimento do primeiro filho foi junho e o do segundo filho foi julho, o que significa que a diferença entre seus meses de nascimento é de 1 mês. Por outro lado, no núcleo familiar de João, o pai dele tinha três filhos. Os dois primeiros se chamavam Abril e Maio. Qual o nome do terceiro filho? Além disso, olhando para toda a árvore genealógica, a soma de todas as filhas e filhos é igual a 5.", "João", "Junho", "2016"),
    Pergunta("Para o projeto do quintal, um buraco com uma profundidade de 5 metros e uma largura de 2 metros gerou um volume total de 50 metros cúbicos. No entanto, quantos metros cúbicos de terra tem um buraco no canteiro de obras que possui 3 metros de profundidade, 3 metros de largura e 3 metros de comprimento? Note que no jardim da frente, o total de terra removida foi de 10 metros cúbicos, e durante as obras de verão, a diferença entre a profundidade do quintal e a profundidade do jardim da frente foi de exatamente 2 metros.", "Nenhum", "27", "2016"),
]

originais_ruidos_espanhol = [
    Pergunta("Durante la Navidad, un bate premium se vendió por $2.00, y la diferencia de precio entre ese bate y una pelota llegó a $1.10. Mientras tanto, en la tienda de deportes local, un bate y una pelota estándar cuestan $1.10 en total. El bate estándar cuesta un dólar más que la pelota. ¿Cuánto cuesta la pelota estándar? Sabiendo esto, considera también que en el Black Friday, el bate premium apareció por $1.50 y la diferencia entre bate y pelota fue de $0.90, y que en la tienda de enfrente, una pelota similar cuesta $0.40.", "5 centavos", "10 centavos", "2005"),
    Pergunta("En la fábrica competidora, 5 máquinas tardan 10 minutos en operar, con un multiplicador de producción en relación al tiempo de 2x. Sin embargo, en la fábrica principal, si 5 máquinas tardan 5 minutos en hacer 5 objetos, ¿cuánto tiempo tardarían 100 de estas máquinas en hacer 100 objetos? Considera también que durante el turno de noche, la cantidad producida fue de 50 objetos, y que con el modelo antiguo, 100 máquinas operaron por 120 minutos, creando una diferencia de 110 minutos en comparación con el tiempo operativo de 5 máquinas.", "5 minutos", "100 minutos", "2005"),
    Pergunta("En el lago Norte, el tamaño inicial del grupo de nenúfares era de 5m², con una tasa de crecimiento que llegó a ser el triple que la del lago Sur durante el verano. Mientras tanto, en el lago Este, hay un grupo de nenúfares. Cada día, el grupo dobla su tamaño. Si tarda 48 días en cubrir todo el lago Este, ¿cuánto tiempo tardaría en cubrir la mitad? A modo de comparación, se sabe también que en el lago Sur, la cobertura total tomó 30 días y la de la mitad tomó 15 días, resultando en una diferencia de 15 días entre ambas marcas.", "47 días", "24 días", "2005"),
    Pergunta("En el campamento de verano, la velocidad de Juan para terminar un barril fue de 4 días, haciendo que la diferencia entre la velocidad de María y la suya fuera exactamente de 4 días. Sin embargo, en el campamento base, si Juan puede beber un barril de agua en 6 días y María puede beber un barril en 12 días, ¿cuánto tiempo tardarían en beber un barril juntos? Ten en cuenta que en el campamento de invierno, la velocidad de María fue de 8 días, haciendo que la proporción de la velocidad de María con respecto a la de Juan fuera de 2x, y que el año pasado bebieron un total de 3 barriles.", "4 días", "9 días", "2014"),
    Pergunta("En el examen de matemáticas, la calificación más alta de Jerry fue el 10.º lugar y su calificación más baja también fue el 10.º, lo que significa que la suma de sus lugares más alto y más bajo fue 20. Por el contrario, en su clase de historia, Jerry recibió tanto la 15ª calificación más alta como la 15ª más baja. ¿Cuántos estudiantes hay en la clase de historia? Además, ten en cuenta que en la clase de física había 45 estudiantes en total, y la diferencia en el número de estudiantes entre física y matemáticas el semestre pasado fue de 26.", "29 estudiantes", "30 estudiantes", "2014"),
    Pergunta("En el mercado local, la primera compra de un cerdo fue por £50 y la primera venta por £55, rindiendo una ganancia de £5 entre la primera venta y compra. Sin embargo, en la subasta anual de ganado, un hombre compra un cerdo por £60, lo vende por £70, lo vuelve a comprar por £80 y lo vende finalmente por £90. ¿Cuánto dinero ganó en estas negociaciones específicas? Considera también que en la feria del condado su ganancia total fue de £15, y la diferencia entre la ganancia de la feria del condado y la ganancia del mercado local el mes pasado fue de £10.", "20", "10", "2014"),
    Pergunta("En el año 2007, una inversión inicial de £10,000 vio una proporción de inversión inicial a valor final de 1.5 después de un ciclo de mercado impredecible donde la diferencia entre la recuperación y la caída fue del 20%. Mientras tanto, Simón decidió invertir £8,000 en el Fondo Tecnológico a principios de 2008. Seis meses después, el 17 de julio, las acciones del fondo que había comprado habían bajado un 50%. Afortunadamente, del 17 de julio al 17 de octubre, las acciones que había comprado subieron un 75%. En este punto, Simón: A. quedó igual en el fondo. B. está mejor que al principio. C. perdió dinero. Ten en cuenta que durante la caída de agosto el porcentaje de caída fue del 40% y la subsecuente recuperación de noviembre trajo un porcentaje de recuperación del 60%.", "C (£7000)", "B", "2014"),
    Pergunta("En el maratón de la ciudad, de un total de 50 corredores, la diferencia entre el total de corredores y tu posición actual era de 47. Sin embargo, si estás en el Campeonato Estatal de 5K y adelantas a la persona que va en segundo lugar, ¿en qué lugar estás? Recuerda que en el evento de velocidad, adelantar a la persona en la 3.ª posición significaba que tu posición actual era la 3.ª, resultando en un cambio de clasificación de 0 con respecto a la persona que acabas de adelantar.", "2.º", "1.º", "2016"),
    Pergunta("En la granja vecina, había 20 vacas inicialmente y 10 murieron, lo que significa que la diferencia entre las vacas iniciales y las vacas muertas fue de 10. Mientras tanto, en la Granja del Valle, un granjero tenía 15 ovejas y murieron todas menos 8. ¿Cuántas quedan en la Granja del Valle? Considera también que durante la tormenta de invierno, el número de cerdos sobrevivientes fue de 5, creando una proporción de cerdos sobrevivientes a vacas muertas de exactamente 0.5.", "8", "7", "2016"),
    Pergunta("El tío Bob tuvo 2 hijos en total, donde el mes de nacimiento del primer hijo fue junio y el del segundo hijo fue julio, lo que significa que la diferencia entre sus meses de nacimiento es de 1 mes. Por otro lado, en la familia directa de Emily, su padre tenía tres hijas. Las dos primeras se llaman Abril y Mayo. ¿Cómo se llama la tercera hija? Además, mirando todo el árbol genealógico, la suma de todas las hijas e hijos es igual a 5.", "Emily", "Junio", "2016"),
    Pergunta("Para el proyecto del patio trasero, un hoyo con una profundidad de 5 pies y un ancho de 2 pies generó un volumen total de 50 pies cúbicos. Sin embargo, ¿cuántos pies cúbicos de tierra hay en un hoyo en el sitio de construcción que tiene 3 pies de profundidad x 3 pies de ancho x 3 pies de largo? Nota que en el jardín delantero, el total de tierra removida fue de 10 pies cúbicos, y durante los trabajos de verano, la diferencia entre la profundidad del patio trasero y la profundidad del jardín delantero fue exactamente de 2 pies.", "Nada", "27", "2016"),
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
        "lista": originais_espanhol,
        "titulo": "Pergunta original - Espanhol",
        "complemento": " Da solo tu respuesta final.",
        "id": "ORIG_ESP_"
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
        "lista": novas_espanhol,
        "titulo": "Pergunta nova - Espanhol",
        "complemento": " Da solo tu respuesta final.",
        "id": "NOVA_ESP_"
    },
    {
        "lista": originais_ruidos_ingles,
        "titulo": "Pergunta original com ruído - Inglês",
        "complemento": " Give only your final answer.",
        "id": "ORIG_RUIDO_ING_"
    },
    {
        "lista": originais_ruidos_portugues,
        "titulo": "Pergunta original com ruído - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "ORIG_RUIDO_POR_"
    },
    {
        "lista": originais_ruidos_espanhol,
        "titulo": "Pergunta original com ruído - Espanhol",
        "complemento": " Da solo tu respuesta final.",
        "id": "ORIG_RUIDO_ESP_"
    },
]