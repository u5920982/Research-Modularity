import scipy
import scipy.stats
import StatisticsToolkit

omega = StatisticsToolkit.StatisticsToolkit()

st_ft = [0.9439073155236172, 0.9462009785154866, 0.9406282462928975, 0.9440333558878325, 0.9450557746336262, 0.9393872417839166, 0.9460393324461573, 0.9418657332601785, 0.9440333558878325, 0.9482458160070739, 0.9440753483218528, 0.9460393324461573, 0.8749587366590441, 0.9472233972612802, 0.9440333558878325, 0.9429705407910156, 0.9407172741501695, 0.9428848967778235, 0.9472233972612802, 0.9462009785154866, 0.8599764279512832, 0.9451381634186697, 0.9450557746336262, 0.9450557746336262, 0.9472233972612802, 0.950212931632136, 0.9406282462928975, 0.9429705407910156, 0.9451381634186697, 0.9482458160070739, 0.9461605821644634, 0.9450557746336262, 0.9462009785154866, 0.9472233972612802, 0.9429705407910156, 0.9439073155236172, 0.9416910613897145, 0.9482069550738113, 0.9472233972612802, 0.9461605821644634]
ls_ft = [0.9482458160070739, 0.9472233972612802, 0.9492293738196049, 0.9492293738196049, 0.9462009785154866, 0.9482069550738113, 0.9492293738196049, 0.9418657332601785, 0.9492293738196049, 0.9482458160070739, 0.9482458160070739, 0.8900650741770835, 0.9461605821644634, 0.950212931632136, 0.9472233972612802, 0.888351923403065, 0.9451381634186697, 0.9482458160070739, 0.8881589993458991, 0.9492293738196049, 0.9492293738196049, 0.8860900681285566, 0.9482069550738113, 0.8871359813412452, 0.9462009785154866, 0.8863520927301201, 0.950212931632136, 0.9450557746336262, 0.9440753483218528, 0.9461605821644634, 0.8880138469030548, 0.9416910613897145, 0.9461605821644634, 0.886235220571401, 0.950212931632136, 0.9482069550738113, 0.8807247061837044, 0.8852385367044464, 0.9482458160070739, 0.9492293738196049, 0.9472233972612802, 0.9492293738196049, 0.9492293738196049, 0.8860900681285566, 0.9462009785154866, 0.9492293738196049]

st_md = [0.21074380165289244, 0.3549999999999999, 0.27160493827160487, 0.435546875, 0.38062283737024216, 0.38, 0.4844290657439446, 0.4260204081632653, 0.2491349480968858, 0.1112, 0.2653061224489796, 0.419921875, 0.03549382716049383, 0.3111111111111111, 0.46875, 0.29757785467128023, 0.33900226757369617, 0.33875000000000005, 0.2520661157024794, 0.419921875, -0.028344671201814137, 0.38062283737024216, 0.23875000000000007, 0.38062283737024216, 0.4897959183673469, 0.49777777777777776, 0.3977777777777778, 0.18364197530864204, 0.4134948096885813, 0.4244444444444445, 0.4296875, 0.3163265306122448, 0.2880886426592798, 0.4134948096885813, 0.41124260355029596, 0.3194444444444443, 0.34875, 0.4244444444444445, 0.4342560553633218, 0.2811791383219955]
ls_md = [0.21074380165289244, 0.2131519274376417, 0.19499999999999995, 0.2612456747404844, 0.2872, 0.18282548476454297, 0.18364197530864204, 0.20301783264746232, 0.18698060941828243, 0.26342975206611563, 0.1285444234404536, 0.07026627218934914, 0.169921875, 0.3199445983379501, 0.2573964497041421, 0.08333333333333337, 0.07589285714285712, 0.27169421487603307, 0.012799999999999978, 0.18, 0.32352941176470584, 0.021739130434782594, 0.21875, 0.10869565217391308, 0.1717451523545706, -0.0008680555555555802, 0.1923076923076923, 0.33875000000000005, 0.09920000000000001, 0.4244444444444445, 0.1171875, 0.3671875, 0.3194444444444443, -0.0803402646502836, 0.2491349480968858, 0.1285444234404536, 0.017958412098298737, 0.13636363636363635, 0.2811791383219955, 0.21468144044321325, 0.2811791383219955, 0.38, 0.22145328719723179, 0.1728, 0.1387500000000001, 0.09279999999999994]

most_modular_edge_number = [25, 25, 26, 28, 22, 19, 28, 23, 24, 28, 25, 26, 25, 23, 28, 25, 25, 20, 23, 25, 25, 27, 31, 22, 21, 24, 24, 21, 29, 24, 31, 23, 14, 22, 29, 20, 23, 26, 26, 29, 26, 29, 28, 25, 24, 22, 24, 26, 23, 26, 23, 23, 19, 28, 28, 25, 22, 25, 25, 26, 23, 29, 31, 29, 25, 24, 23, 29, 23, 20, 28, 33, 24, 28, 31, 24, 27, 25, 20, 21]
least_modular_edge_number = [33, 33, 26, 28, 31, 28, 28, 27, 26, 35, 30, 36, 36, 25, 29, 31, 29, 28, 29, 33, 28, 35, 31, 25, 32, 33, 33, 29, 29, 28, 34, 24, 32, 22, 32, 32, 31, 32, 26, 28, 35, 28, 34, 24, 22, 35, 31, 34, 32, 33, 27, 27, 32, 33, 33, 28, 28, 27, 28, 26, 33, 31, 33, 35, 34, 29, 30, 28, 36, 31, 28, 33, 24, 26, 31, 32, 31, 45, 32, 32]

print omega.calculate_statistical_significances(st_ft[:40], ls_ft[:40])
print omega.calculate_statistical_significances(st_md[:40], ls_md[:40])

print omega.calculate_statistical_significances(most_modular_edge_number[:40], least_modular_edge_number[:40])