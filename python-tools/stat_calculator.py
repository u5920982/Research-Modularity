from StatisticsToolkit import StatisticsToolkit
import tools.storage.stat_warehouse as stat_warehouse
import tools.storage.fitness_warehouse as fitness_warehouse

statistics_toolkit = StatisticsToolkit()
print 'len of values 1: ', len(fitness_warehouse.stoc_p00_by_dist_p00_final)
print 'len of values 2: ', len(fitness_warehouse.elite_stoc_p00_by_dist_p00_final)

list_1 = [-0.9603614262983307, -0.696933286008954, -0.2952608688392861, -0.8346917413730194, -0.7602416631280676, -0.7961914305756238, -0.7218473312549878, -0.9417927535170155, -0.8044697599886272, -0.8716970181334505, -0.829716825646148, -0.8366330648769603, -0.8964532128835496, -0.8281401794340602, -0.9407406266312023, -0.8770135772171543, -0.9606357146871792, -0.9340013643489411, -0.7591511330851448, -0.02992598194036855, -0.6821222303736751, -0.9717080429018942, -0.8542234253205551, -0.9247157710567324, -0.9222931489312449, -0.7510147021054312, -0.780150059178229, -0.7779828420017058, -0.7281337537898752, -0.8587880289252123, -0.8288159318555386, -0.7446925304312825, -0.9086259645542056, -0.9018505333758396, -0.9008934722633014, -0.7620866703870854, -0.7819558301949086, -0.874752461129891, -0.8103634903785752, -0.6005135046512458, -0.9191089584469548, -0.911705960546867, -0.6950466046911259, -0.9307985209940808, -0.6323546723056308, -0.8182903982004838, -0.721025575907208, -0.9054920563042673, -0.8927318889215142, -0.9435692014261727, -0.8777602107189907, -0.5466508522063358, -0.6649650614023549, -0.7900276842395512, -0.8963461910422412, -0.8458234006517423, -0.9365086161932047, -0.48549301936278993, -0.9388991745099035, -0.7029954403944829, -0.668319334588672, -0.737661829995735, -0.18937400071934932, -0.1959028247753434, -0.904155952191879, -0.6428747202366171, -0.943899756217776, -0.9258777901856939, -0.850788027548643, -0.9199031487247332, -0.8531165302998577, -0.7760050426792033, -0.9654047446553581, -0.8335548756979769, -0.3017339806429168, -0.9547824524465339, -0.9097262237764584, -0.9081141075559467, -0.7851808971770362, -0.791993099441021, -0.7851058575940865, -0.7326559178189161, -0.8639395274965534, -0.654065908464438, -0.805837484175125, -0.9009520452505154, -0.8262768778601334, -0.8819449258436984, -0.6880433629114421, -0.6271324021086566, -0.6863698428775283, -0.9058244112119659, -0.8385173871655969, -0.9370177207402247, -0.764669150304241, -0.7796021584061114, -0.7180624630860081, -0.794150880995689, -0.7856974039221689, -0.5765935042252672]
list_2 = [-0.9603614262983307, -0.6925613143526766, -0.2952608688392861, -0.8346917413730194, -0.7602416631280676, -0.7961914305756238, -0.7218473312549878, -0.9417927535170155, -0.8044697599886272, -0.8716970181334505, -0.829716825646148, -0.8366330648769603, -0.8964532128835496, -0.8281401794340602, -0.9407406266312023, -0.8758388480751937, -0.9606357146871792, -0.9271812734004873, -0.7487202594098512, -0.027634107348845943, -0.6821222303736751, -0.9724921415210683, -0.8542234253205551, -0.9247157710567324, -0.9222931489312449, -0.7445438893918124, -0.7684999296014962, -0.7779828420017058, -0.741125336602464, -0.8675475285384772, -0.8288159318555386, -0.7446925304312825, -0.9053681339177868, -0.9018505333758396, -0.8955124733470499, -0.7620866703870854, -0.7819558301949086, -0.8800516747011802, -0.8103634903785752, -0.6005135046512458, -0.9191089584469548, -0.911705960546867, -0.6950466046911259, -0.9307985209940808, -0.6323546723056308, -0.8182903982004838, -0.7262785996456385, -0.9067200952488383, -0.8927318889215142, -0.9413011504415886, -0.8777602107189907, -0.5277286458039797, -0.6649650614023549, -0.7900276842395512, -0.8963461910422412, -0.8416045043072389, -0.9292263660444133, -0.5052352805414494, -0.935285648211407, -0.6968683227547671, -0.6828064820097811, -0.737661829995735, -0.18937400071934932, -0.1959028247753434, -0.9361893476877003, -0.6428747202366171, -0.9433969495776913, -0.9258777901856939, -0.850788027548643, -0.9199031487247332, -0.8531165302998577, -0.7760050426792033, -0.9652182657657437, -0.8335548756979769, -0.3017339806429168, -0.9547824524465339, -0.9097262237764584, -0.9081141075559467, -0.7722060342155075, -0.791993099441021, -0.8037147455177435, -0.7326559178189161, -0.8506050311954728, -0.654065908464438, -0.805837484175125, -0.9009520452505154, -0.8262768778601334, -0.8819449258436984, -0.6880433629114421, -0.6271324021086566, -0.6863698428775283, -0.9058244112119659, -0.8398829040345757, -0.9370177207402247, -0.736522682965191, -0.7822324811306202, -0.7065996495121786, -0.794150880995689, -0.7856974039221689, -0.582337388403047]
list_3 = [-0.9545154851235227, -0.665786126763304, -0.27374789202861965, -0.7557480855763408, -0.7091219147143789, -0.7558371453330821, -0.7859742850598072, -0.9438695808251959, -0.7925262889535389, -0.8869357046943206, -0.8118481880821394, -0.7254182671143533, -0.881779026112229, -0.8362111355296508, -0.9475412672829362, -0.8899652138643829, -0.9571694371013441, -0.8948175540293939, -0.6674984922714328, 0.10154490853358462, -0.5372511557700147, -0.954861790733211, -0.8914728045120848, -0.9098867676442807, -0.8998646631058796, -0.6588084193536741, -0.6481299089816777, -0.762352709323994, -0.736161924826204, -0.8906526467917611, -0.7628299980853493, -0.8018709165716189, -0.9107746128485699, -0.9159947884242656, -0.8956757476808119, -0.7660716819904887, -0.7444820648684388, -0.8588925245337217, -0.7110441712000886, -0.5095308456422107, -0.9151265162011838, -0.9157692549643134, -0.6490905828950162, -0.9455022146683258, -0.6966709490669107, -0.6375099816386538, -0.6519369220322476, -0.9232221315092749, -0.8918083629547131, -0.9408732984410978, -0.8542768141730492, -0.4958899014071995, -0.6558912039091925, -0.7494454657664652, -0.9179062788901291, -0.8380004552487927, -0.9296316412121021, -0.5039616291354374, -0.9274809054237155, -0.723129314531777, -0.6512534386252756, -0.7829862193641269, -0.16640397505675808, -0.21559739775093634, -0.9592434511058672, -0.5940351565408316, -0.8708776805036741, -0.8922723343141428, -0.7900916660420684, -0.8743387947801011, -0.7985155323403799, -0.6216820137567295, -0.9433263810370953, -0.8159035768113501, -0.18728381721891804, -0.9432319905786302, -0.9045049163623932, -0.9178787172203364, -0.8009485749141068, -0.7978974834263418, -0.8114434528714005, -0.8084021211085846, -0.8585601851962946, -0.6023374560993037, -0.8570629064857291, -0.8239006326149637, -0.8868911676327391, -0.8798426183208035, -0.6053307496035633, -0.5603308358372585, -0.6536457802399298, -0.9164771498455335, -0.8661868894123838, -0.9407194013765259, -0.6437913700443174, -0.7252234590485129, -0.7097226095692584, -0.773274475314956, -0.798087422650409, -0.6187870583024238]

print statistics_toolkit.calculate_statistical_significances(list_1,
                                                             list_2)