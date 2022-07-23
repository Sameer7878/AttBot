import datetime
import pytz
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

register_id = {'mj.che_vr73304': '21KB1A1248', 'jst_call_me__mahi': '21KB5A0124', 'h_o_n_e_y_1_3_5': '21KB1A05H6', 'alludu._.07': '20KB1A0218', 'nithinpodavakam': '20KB1A0388', 'life_of_lokesh18': '20KB1A0142', 'mohith_mohi_x': '21KB1A04A7',
               'sudeepthi__narayana': '20KB1A1242', 'rithwik_1221': '20KB1A1258', '_.sohail077._': '21KB5A0112', '_i_am_mr_aloner_': '20KB1A03C1', 'its_me_princess_1573': '20KB1A0516', 'bhavana_chowdary_7': '21KB1A3015', 'mr_yash_6309': '21KB5A0324', '_little_princess_lover_': '20KB1A0154', 'lucky.lucky1267': '20KB1A04A3', 'chittithelover': '20KB1A0335', 'apuroop_pandu': '19KB1A05C7', 'mr__attitude___max_': '20KB1A0402', 'mehraj___shaik': '21KB1A3083', 'mr.photoholic_ajay_': '20KB1A0339', 'bhanu_bunny_17': '21KB1A0567', 'madeshnelavala': '19KB1A1231', 'saketh169': '21KB1A0319', 'abhi_karate03': '20KB1A1210', '_mr_m_o_n_k_21_': '19KB1A05B6', 'upendra_____2': '19KB1A04E3', 'urs_truly_himakumar': '21KB1A04B2', 'balu_bellamkonda': '19KB1A0308', 'ajmad7268': '21KB5A3004', 'lover_of_psycho_45': '21KB1A0477', 'vineeth_karanam_': '19KB1A0122', 'yedukondalu3634': '21KB1A0227', 'a__.r_.u_.n__': '19KB1A1222', '_hemanth_yadav__': '20KB1A0367', 'prudhvi7391': '20KB1A0329', '_iambabbu': '21KB1A0553', 'sai_stylish_28': '19KB1A0375', 'dr_comrade__loki_106': '20KB1A0106', 'tharun6744': '19KB1A1216', 'venkatesh_chevuru': '20KB5A0327', '_____lm_lucky_____': '20KB1A0419', 'nandini_reddy_koduru': '21KB1A0271', 'ja_ya9725': '20KB1A3011', 'mr_swaroop_silent': '19KB1A0570', '_soul_hacker_giri_': '20KB1A0351', 'honeyrdx7': '20KB1A0305', 'haripulluru': '21KB1A0263', 'k.sivaprasad_12345': '21KB1A0464', 'vamsi_krishna_m589': '21KB1A0589', 'saketh_reddy0908': '20KB1A3012', '_akshay__reddy123_': '21KB1A0474', 'mr_queen_less_bhanu': '19KB1A0493', 'wiz_kidoo_': '20KB1A03B5', '_the_raptor._': '20KB5A0218', 'rebelstarsunny': '21KB1A0333', '_umamahesh___': '20KB1A0548', 'sam_.r._13': '21KB5A0325', 'k.asrithareddy': '21KB1A0563', 'shaik_yakhoob___': '19KB1A05F6', 'precious__sai__05': '20KB1A3060', '__tharun_kumar_b': '19KB1A0415', 'mr.enfielder_6225': '19KB1A1254', 'gnana_prasunambika.dupati': '21KB1A0539', 'sujana__sujju_': '20KB1A3023', 'naveensathyaveti': '21KB5A0321', 'gani.ramireddy': '19KB1A05D3', 'mr_lucky_davood__': '19KB1A0154', 'journey__lover__reddy': '19KB1A0165', 'sameeulla76': '19KB1A0157', 'surekha_0220': '20KB1A3052', '_eyes_roller': '19KB1A0332', 'natural_rock_star_chintu': '19KB1A0307', 'am_harsha_09': '19KB1A0373', '_raja__reddy_': '19KB1A0301', '_harsha_chowdhary_': '21KB1A0285', 'balu.97197': '19KB1A0344', 'prakashyadav_6303': '20KB5A0337', 'swagking1817': '21KB1A0584', 'pranathibathala': '21KB1A0207', 'chinthaneerajaa': '20KB1A0524', '___urs__friendly__surendra___': '21KB1A0493', 'akhil_sanni': '20KB1A3046', '_j__2002._': '20KB1A0425', 'dinesh_ravilla_99': '21KB5A0339', 'rithwick_reddy_143': '21KB1A0327', 'user_not_found_x20': '19KB1A1244', 'future_aviator_karthik': '21KB5A0342', 'vishnu_teja__reddy': '19KB1A1229', 'srikanth_sree012': '20KB1A0201', 'dheerajkrishna0492020': '19KB1A1223', 'revanth____007': '20KB1A0283', 'its_mehemuuu': '19KB1A04G3', '__lovable_i_d_i_o_t__': '20KB1A1204', 'jyothi886677': '20KB1A0205', 'reddy___gari___abbay___': '20KB5A0315', 'challa_is__the_brand': '21KB1A0424', 'p_mahendra_143': '21KB1A04A4', 'b_h_a_n_u_prakashreddy': '19KB1A04J1', 'muni_volley_8': '21KB1A04C0', 'inid2022': '21KB1A0460', 'v_e_n_k_y_1626': '19KB1A0558', 'jaswanth_sai30': '20KB5A0201', 'lalith_allias_karan_3': '21KB1A1212', 'khaliqss': '19KB1A1240', 'j.a.y.a.n.t.h__': '21KB1A0419', 'likith.45': '20KB1A03B9', 'dorababu_0831': '20KB5A0403', '5u34n_': '19KB1A0521', 'vishnuvardhanmalipati': '20KB1A0487', 'niharika_challa_niha': '20KB1A3008', 'sweety__1229': '21KB1A0513', 'sushwanth_k_u_m_a_r': '19KB1A05H3', 'ramprakashreddy45': '19KB1A1230', 'prsnakmr_918': '19KB1A04C0', 'kingwithoutacrown_2k03': '21KB1A04G2', 'sk.nawaz702': '20KB1A04F6', 'p_e_a_c_e_l_i_f_e__': '21KB1A0465', '_mr.__reddy': '20KB1A3044', 'ajay_adeppagari': '20KB1A0404', 'harsha._.official': '20KB1A0217', 'hari_krishna_789': '20KB1A0287', 'harsha__073': '21KB1A30A0', 'shaolin_smaran': '19KB1A1202', 'chegueverachaitanya': '19KB1A1204', 'prudhvirajhasthi': '19KB1A1211', 'yogeeshamuluru': '20KB1A0304', 'call__me__diggi': '20KB1A0269', '_jash_217': '19KB1A05B6', 'venkata__vasanth': '20KB1A0216', 'smile._.killer._.07': '20KB1A0217', 'sasikiran_2003': '20KB1A0522', '_charan_cj_6': '21KB1A0426', 'sahoresuraj': '20KB1A0114', 'panee_9': '20KB1A0438', 'ravi4tr': '21KB1A0249', 'sukumar_royals': '19KB1A0327', '__dynamic_killer__': '21KB1A0330', 'saketh_papareddy': '19KB1A1233', '_surya_suri_789': '20KB1A3051', '_lalith_kumar_reddy_': '21KB1A1212', 'dhinakar__sai': '20KB1A0423', 'heart.hacker_008': '20KB5A0329', 'u_ravi.teja': '20KB5A0140', 'rameez.shaik_': '20KB1A05F4', 'muralikataru': '21KB1A1225', 'pavan_tony_123': '21KB1A1243', 'call_me_poriki___420': '21KB1A04C0', 'my_life_my_rules_46_': '21KB1A0344', 'i_am.nadendla': '20KB1A04A9', 'alwaysjyothish': '21KB1A05I1', 'rahulsurya121': '21KB1A05B4', 'rajeev_92223': '21KB1A0599', 'dad_calls_me_chotu': '21KB1A05F2', 'sumanth5723': '21KB1A0459', 'crazy_boy_jashu': '21KB1A0444', 'sreekanth_leburu': '20KB5A0354', 'sole_soul__3': '21KB1A0481', 'yashuyaswanth1290': '20KB1A0429', '__liyaz_syed__': '20KB1A3055', 'lucky.charm827': '20KB1A04A3', 'revanth.reddy_2405': '19KB1A0513', '_sathvik_777_': '21KB1A1238', 'rock_star_1433_': '21KB1A0238', 'saradhi__v': '19KB1A04I4', 'alone__heart_kishore': '21KB1A1207', 'ch.badri.338': '21KB1A0434', 'sumanthsahho': '21KB1A0584', 'sasi_lxn_455_': '20KB1A0455', 'rockybhai.chandu.52': '21KB1A0293', 'u_rs_lovingly_tharun': '21KB1A1248', 'deepamdeepthi_': '21KB1A3001', 'pradeep_0321': '19KB1A04E6', 'harsha_lebur': '21KB1A0585', 'p.jagadeesh_naidu': '21KB1A1241', 'bigil_008': '21KB1A0476', 'itsme_nawaz53': '20KB1A04F5', 'dreamer_.o4': '20KB1A0502', '_mr_rpm_breaker': '20KB1A03B7', '_chethan_14_': '20KB1A0592', 'loyal__guy_': '20KB1A0427', 'mr.bob_0051': '21KB1A0351', 'loyal_one_praveen': '21KB1A0241', '__babbu____prs': '21KB1A0518', 'akashakash193119': '21KB1A0240', 'happysoul2801': '20KB1A05E3', 'saad_ahamed_syed': '21KB1A0339', 'priyatham_2002': '20KB1A0515', 'im_loki_08': '21KB1A1204', 'a_r_s_h_a_d_s_h_a_i_k': '21KB1A0269', 'bhanuchand.23132': '20KB1A0356', 'sajid_hussain_08': '20KB1A0370', 'parvaz_shaik': '20KB1A04F8', 'kvinayrajj': '20KB1A0464', 'its_me_ss_rowdy': '19KB1A1244', 'suchakridharreddykonduru': '20KB1A0240', 'darling_aniish': '20KB1A1222', 'prem.kumar7830': '21KB1A0449', 'attiutude_king_sai': '21KB1A0403', 'crazy_nick990': '21KB1A0456', 'always_yagna': '19KB1A05I8', 'swe.ety9735': '21KB1A05H0', 'saijaguar.135': '19KB1A1218', 'suresh_reddy_guvvala_': '20KB1A0347', 'vinaycherry143': '21KB5A0332', 'dha1528': '21KB5A0304', 'khushi_sharma2409': '21KB1A0569', 'sujith_v_ch': '21KB1A0430', 'mr.dead_rine_007': '19KB1A0498', 'vemula_na_ni': '19KB1A1252', 'k_rant_hi': '21KB1A1245', 'bindu_madhav_raju': '21KB1A1203', 'ha__rs__hi__tha__37': '21KB1A0571', 'attitude_queen__2503': '21KB1A05C6', 'rishi_kumar_c_e_o': '21KB1A0217', 'yamunaarava6': '19KB1A0322', 'parrot__kt': '20KB1A05C4', 'anon_dhanush__': '20KB1A3019', 'dhaksha_09': '20KB1A1218', 'akhila_neeluru': '20KB1A0599', 'rajuyatham8': '21KB1A04H0', 'jayakrishna.jai.79': '21KB5A0102', 'loveshot7_': '21KB1A0342', 'rajeev_nine9': '21KB1A0599', 'duddu_madhavi': '21KB1A0536', 'chamarthi_yashu': '20KB1A0518', 'deepthireddy_atla': '20KB1A0410', 'shaik_hussain__143': '21KB1A3066', 'n._.identity': '19KB1A0114', 'hemanthbdvm': '20KB1A0596', 'inside_lover999': '21KB1A0467', '_crazy.vinay_': '21KB1A0348', 'jeevith_rebel': '21KB1A0332', 'h_emanth_n': '20KB1A05C4', 'pradeepnaidu1432': '21KB1A0132', 'yogesh_vijay2001': '19KB1A0348', 'delphi_gracy': '21KB1A0226', 'priya_______1188': '21KB1A0206', 'hemu.msd': '21KB1A3044', '__ganesh.03__': '20KB1A04I2', '_yaswanth__reddy__': '19KB1A1250', 'jagadeesh4835': '20KB5A0336', 'balaramreddy__._._': '19KB1A1232', 'jagadeesh_.naidu': '21KB1A1241', '__a._.k_47': '19KB1A0576', 'khalid_0_3_0': '20KB1A03A1', 'thenameisvalivulla': '20KB1A03A6', 'mr.bhargava__2004': '21KB1A3047', 'sr_sarvotham_reddy': '19KB1A04C8', 'chennaiah21': '19KB1A04E1', 'kole_rajasekhar_19': '19KB1A0349', 'dynamo_sasi': '19KB1A0554', 'm.r_idiot_143': '21KB1A05I3', 'saisankarvayugundla': '20KB5A0316', 'devaki_thumati': '21KB1A3041', 'keerthi__reddyyy': '19KB1A1220', 'mr.black_611': '21KB1A0270', 'decoit_one': '21KB1A0217', 'girish_reddy_gangavaram_321': '20KB5A0350', 'prbindu5': '21KB1A0204', 'si.nce_2001': '19KB1A0385', 'truegirl398': '21KB1A0445', 'krishna_makani98': '19KB1A0585', 'mr_frustrated_soul._': '20KB1A0402', 'saikummar05': '20KB5A0325', 'itsmekeertan': '21KB1A0549', 'chaitu_royal_14439': '21KB1A0341', 'ram1091charan': '20KB1A05A5', 'krishaveni55': '20KB1A05A4', 'king_shaik_777': '21KB1A1247', 'nithish.raju.2003': '21KB1A0521', 'i_am_udaykumar_chowdary': '21KB5A0331', 'its_mee_sekhar': '20KB1A1246', '___p.a.n.d.u_loves___': '19KB1A05G9', 'rohi_preethi_2504': '21KB1A05C6', 'jyothiathmakuru': '20KB1A0205', 'jannath_hussen': '21KB5A0336', '__.__jasmine_.__': '19KB1A05F0', 'tinygirlstyle': '19KB1A1214', '_h.o.n.e.y_l.o.v.e.s_': '19KB1A0261', 'oye__its__me__akhil': '20KB1A0130', 'akhila_oo1': '19KB1A1215', 'cool________angel': '19KB1A0146', 'rakshana__chowdary_': '19KB1A0439', 'vamsi_yadav_ulsa_049': '21KB5A0311', '_s_i_s_i_n_d_r_i___009': '21KB1A1202', 'hari_9400': '21KB1A1236', 'naveen__yenuganti': '19KB1A1255', '__r_o_c_k_y______': '19KB1A05E3', 'hemanth_chandra_00': '21KB1A1210', 'volley_lover_uday._ud': '21KB1A1211', 'prasanthchalla143': '21KB1A1215', 'warm_walker_': '20KB5A0366', '__game_boy__yash': '21KB5A0324', 'ganeshannabathina': '21KB1A0204', 'achukrishnamma': '20KB1A05A7', '20kb1a0402': '20KB1A05A8', 'urs_truly_yokshith': '21KB1A1224', 'sai_star_1233': '21KB1A3023', 'iamdheerajkrishna': '19KB1A05C2', 'sudheerbabu7797': '19KB1A04D8', 'majestic_king_nari': '21KB1A0528', 'narahari1801': '21KB1A0408', 'miss_waste_3': '21KB1A0481', 'bharath_kumar_ry': '21KB5A0338', 'bhargav_sarvepalli': '21KB1A3080', 'bhavaniprasad594': '20KB1A0594', 'sushma_muppala': '20KB1A0593', 'world_of_adarsh_vikas': '20KB1A0338', 'pramodh_kole': '20KB1A0473', 'i_am_teja_yy4s': '21KB5A1206', 'anji4469': '21KB5A1202', 'brokenboy_sudheer_': '20KB5A0214', 'sujith__duvvuru': '20KB1A0220', 's_a_i_t_e_j_a_77': '20KB1A1208', 'anu_anvi2645': '20KB1A0209', 'kowshik.ganesh': '19KB1A05C4', 'sw_eety1836': '20KB1A0241', 'durgapriya479': '20KB1A0245', 'tejoday4': '20KB1A0239', 'devil_moon_81': '20KB1A3027', 'dakshayani_raj': '20KB1A0565', 'munikrishna365955': '20KB1A0202', 'sowmya_kurucheti': '21KB5A0413', 'stark_mark_4': '20KB1A0290', 'bobby.nandigam': '20KB1A0595', 'its_me_ur_comrade': '21KB1A0312', 'attnbkr222': '19KB1A1221', 'harsha____vip': '21KB1A0256', 'keerthipati_mahidhar': '20KB1A1228', 'i_am.siva_': '21KB5A1203', 'duddu_madhavi_113': '21KB1A0536', 'yegireddy_nani': '21KB1A04H1', 'saiesh____11': '19KB1A0322', 'hemanthm2003': '20KB1A0371', 'v.k_r_i_s_h_n_a__chowdary': '21KB5A1204', 'local_abbai_avinash': '19KB1A0329', 'shamsheer_shaik_07': '20KB5A0404', 'manoj___manoj__': '20KB5A0224', 'infinitesoulboy_01': '21KB1A0337', 'bharath.pr_in_ce11': '20KB1A0212', '_shr_avankumar': '21KB5A0218', 'megha_meghanadham': '21KB5A0409', 'siddu_sreedhar_reddy': '21KB5A0107', 'bhuvan_sai_01': '21KB1A3023', '_hema_nandini_': '20KB1A0534', 'ma__nogna': '20KB1A0566', 'divyanth_pathipati': '20KB1A3038', 'greeeshhhuuu': '20KB1A05B9', '_mr.chanduyadav_': '21KB1A0293', 'dha3sh': '20KB1A3030', 'sripathi_vamsi': '21KB1A04E5', 'nitenkumar58': '21KB1A05B8', 'murali_mono17': '20KB5A0226', 'bunny_vira': '21KB1A0584', 'ravan_asura_2': '19KB1A0319', 'vijji_1408': '19KB1A0210', 'prasanth__0552': '20KB1A3058', 'hemanthreddy1437': '21KB1A05I9', 'chandu_reddy_11': '20KB5A0232', 'gowtham_reddy_17': '21KB1A05C3', 'sairam_chevuri': '19KB1A1203', '07_hari_krishna': '20KB1A0287', 'pavan_yadav622': '20KB1A1255', 'ismart_yash_1207': '20KB5A0360', 'killer.__.dhanush': '20KB1A0383', 'm_r___k_k': '21KB1A0469', 'asif_bhai_vr46': '19KB1A1244', 'sai_2_1_': '19KB1A05I4', 'swing_shifter': '21KB1A0567', 'its_me_indu1': '19KB1A0421', 'she_call_me_hari546': '20KB1A0546', 'jaswanth_smart_1': '21KB1A0102', 'marvelous_guy_harshith_': '20KB1A0445', 'veerawarrior1011': '21KB1A0305', 'akhil._17': '20KB1A3041', '___krish__sai___': '20KB1A0590', 'shiva______sshiv': '20KB1A04B3', 'mr___vivekvikky': '20KB1A0111', 'h_hemanth_n': '20KB1A0592', 'peramalasettyvignesh': '21KB1A05D2', 'sreeja._604': '20KB1A0482', '____urs__truly__dinesh____': '21KB1A0475', '__romeo.____': '21KB1A3007', 'mahendra__1891': '21KB1A0466', 'kavya__reddy_9': '21KB1A3030', 'dileepking29': '20KB1A0541', 'yogeswar__reddy__': '21KB1A04B4', 'na_ve_en_sai_54': '21KB1A04B3', 'decent_boy_kittu96': '21KB1A0596', 'spmtsanthosh': '20KB5A0240', 'innocent_boy_lokii143': '21KB1A0480', 'dinesh.sandi': '21KB1A04C4', 'harshavardhanreddy____': '20KB1A05G5', 'hemanth_2109_msd': '21KB1A0592', 'hang_over__mind': '21KB1A0324', 'venkatasai6304': '21KB1A05A0', '_sathwik__': '20KB1A1233', 'its__me__sravan_': '20KB1A0363', '_itz.chin': '21KB1A0565', '_s_h_o_u_k_a_t_h_a_l_i_': '21KB1A0560', '_ray_shiki': '20KB1A0210', 'batta_yadav': '21KB1A0415', 'harsha_vardhan_korapati': '21KB1A0580', 'praveen_1289': '21KB1A0412', 'ig_rithwik': '19KB1A05J3', 'poorna_navanari': '21KB1A0321', 'chanduyadav5619': '20KB5A0227', 'raju3869yadav': '20KB1A0301', 'gova__3': '20KB1A0250', 'vegurusukumar': '21KB1A05I8', 'vinay_chepuru': '20KB5A0327', 'happiest_balu': '20KB1A0166', 'sameer_shaik__12': '21KB1A04E0', 'bunny_quien': '21KB1A0571', 'cute_girl__vinni': '21KB1A3014', 'm_r____c_o_o_l': '21KB1A04A2', 'rishi_reddy_121': '19KB1A0316', '_innocent__leap_': '21KB5A0211', 'chandramuni2204': '21KB5A0337', 'nikhilesh_yadav_555': '20KB1A05G9', 'chandu_candy_731': '20KB1A0125', 'its__naani_s': '21KB1A0450', '__dhan_reddy_47': '21KB1A05E5', 'bharath_prince_11': '20KB1A0212', 'diggi__edits': '20KB1A0253', 'vikas_gosula': '21KB1A0454', 'sampath_kumar_jogi_9798': '20KB1A0229', '_janani.reddy': '19KB1A0569', 'nanda_reddy__143': '21KB1A0289', 'saikumar_malli': '21KB1A0247', '_mr_manjunadh_': '20KB1A0277', 'sravankumarannameti': '20KB1A3004', 'lucky.lucky1118': '20KB1A04A3', '__yaswanth__pspk__': '21KB1A0287', 'dhan_reddy47': '21KB1A0289', 'bhanuprakashreddyam': '20KB1A0303'}
temp_register_id = {}
time_slot_bookings = ['dhan_reddy47', 'mohith_mohi_x', 'sudeepthi__narayana', 'i_am.nadendla','varnith392', '_sai_010', 'i_am.nadendla','07_hari_krishna', '5u34n_', '_.sohail077._', '____urs__truly__dinesh____', '___krish__sai___', '___urs__friendly__surendra___', '__a._.k_47', '__babbu____prs', '__dhan_reddy_47', '__game_boy__yash', '__liyaz_syed__', '__lovable_i_d_i_o_t__', '__romeo.____', '_akshay__reddy123_', '_charan_cj_6', '_chethan_14_', '_crazy.vinay_', '_h.o.n.e.y_l.o.v.e.s_', '_hema_nandini_', '_itz.chin', '_j__2002._', '_janani.reddy', '_jash_217', '_mr.__reddy', '_mr_m_o_n_k_21_', '_mr_manjunadh_', '_mr_rpm_breaker', '_raja__reddy_', '_ray_shiki', '_s_h_o_u_k_a_t_h_a_l_i_', '_sathvik_777_', '_sathwik__', '_soul_hacker_giri_', '_surya_suri_789', '_yaswanth__reddy__', 'a__.r_.u_.n__', 'ajay_adeppagari', 'akashakash193119', 'akhila_neeluru', 'always_yagna', 'alwaysjyothish', 'am_harsha_09', 'anji4469', 'anon_dhanush__', 'anu_anvi2645', 'apuroop_pandu', 'balaramreddy__._._', 'batta_yadav', 'bhanu_bunny_17', 'bhanuchand.23132', 'bhanuprakashreddyam', 'bharath.pr_in_ce11', 'bharath_kumar_ry', 'bharath_prince_11', 'bhargav_sarvepalli', 'bhavaniprasad594', 'bhuvan_sai_01', 'bigil_008', 'bobby.nandigam', 'brokenboy_sudheer_', 'bunny_quien', 'call__me__diggi', 'ch.badri.338', 'challa_is__the_brand', 'chamarthi_yashu', 'chandu_reddy_11', 'chanduyadav5619', 'chegueverachaitanya', 'chennaiah21', 'chinthaneerajaa', 'cool________angel', 'dakshayani_raj', 'decent_boy_kittu96', 'deepthireddy_atla', 'dha1528', 'dha3sh', 'dheerajkrishna0492020', 'dhinakar__sai', 'diggi__edits', 'dileepking29', 'dinesh.sandi', 'dinesh_ravilla_99', 'divyanth_pathipati', 'dorababu_0831', 'dr_comrade__loki_106', 'dreamer_.o4', 'duddu_madhavi', 'duddu_madhavi_113', 'durgapriya479', 'future_aviator_karthik', 'gani.ramireddy', 'girish_reddy_gangavaram_321', 'gnana_prasunambika.dupati', 'gova__3', 'greeeshhhuuu', 'h_emanth_n', 'h_hemanth_n', 'ha__rs__hi__tha__37thenameisvalivulla', 'happysoul2801', 'hari_krishna_789', 'harsha._.official', 'harsha_lebur', 'harsha_vardhan_korapati', 'heart.hacker_008', 'hemanthbdvm', 'hemanthm2003', 'hemu.msd', 'i_am.siva_', 'i_am_teja_yy4s', 'i_am_udaykumar_chowdary', 'iamdheerajkrishna', 'infinitesoulboy_01', 'innocent_boy_lokii143', 'ismart_yash_1207', 'its__me__sravan_', 'its__naani_s', 'its_me_indu1', 'its_me_princess_1573', 'its_me_ur_comrade', 'its_mee_sekhar', 'itsme_nawaz53', 'j.a.y.a.n.t.h__', 'ja_ya9725', 'jeevith_rebel', 'jyothiathmakuru', 'k.asrithareddy', 'k.sivaprasad_12345', 'keerthi__reddyyy', 'khalid_0_3_0', 'khaliqss', 'khushi_sharma2409', 'killer.__.dhanush', 'kowshik.ganesh', 'krishna_makani98', 'likith.45', 'local_abbai_avinash', 'loveshot7_', 'm_r___k_k', 'ma__nogna', 'madeshnelavala', 'mahendra__1891', 'majestic_king_nari', 'manoj___manoj__', 'miss_waste_3', 'mr.bhargava__2004', 'mr.bob_0051', 'mr.dead_rine_007', 'mr.enfielder_6225', 'mr.photoholic_ajay_', 'mr_frustrated_soul._', 'mr_lucky_davood__', 'muni_volley_8', 'munikrishna365955', 'murali_mono17', 'na_ve_en_sai_54', 'nanda_reddy__143', 'nandini_reddy_koduru', 'natural_rock_star_chintu', 'naveen__yenuganti', 'naveensathyaveti', 'nithish.raju.2003', 'oye__its__me__akhil', 'p_e_a_c_e_l_i_f_e__', 'p_mahendra_143', 'panee_9', 'parrot__kt', 'parvaz_shaik', 'peramalasettyvignesh', 'poorna_navanari', 'pradeep_0321', 'pradeepnaidu1432', 'prasanth__0552', 'prasanthchalla143', 'praveen_1289', 'precious__sai__05', 'priyatham_2002', 'prsnakmr_918', 'rajeev_92223', 'rajeev_nine9', 'rakshana__chowdary_', 'ramprakashreddy45', 'ravi4tr', 'rebelstarsunny', 'reddy___gari___abbay___', 'revanth.reddy_2405', 'revanth____007', 'rithwick_reddy_143', 'rithwik_1221', 's_a_i_t_e_j_a_77', 'sahoresuraj', 'saisankarvayugundla', 'sajid_hussain_08', 'saketh_papareddy', 'saketh_reddy0908', 'sam_.r._13', 'sameer_shaik__12', 'sampath_kumar_jogi_9798', 'sasi_lxn_455_', 'sasikiran_2003', 'shaik_yakhoob___', 'shamsheer_shaik_07', 'shaolin_smaran', 'she_call_me_hari546', 'si.nce_2001', 'siddu_sreedhar_reddy', 'sk.nawaz702', 'sole_soul__3', 'sowmya_kurucheti', 'spmtsanthosh', 'sravankumarannameti', 'sreeja._604', 'sreekanth_leburu', 'srikanth_sree012', 'sripathi_vamsi', 'stark_mark_4', 'suchakridharreddykonduru', 'sujana__sujju_', 'sujith__duvvuru', 'sujith_v_ch', 'sumanthsahho', 'surekha_0220', 'sushma_muppala', 'sushwanth_k_u_m_a_r', 'sw_eety1836', 'swagking1817', 'sweety__1229', 'tharun6744', 'thenameisvalivulla', 'u_ravi.teja', 'user_not_found_x20', 'v_e_n_k_y_1626', 'vamsi_krishna_m589', 'veerawarrior1011', 'vemula_na_ni', 'venkatasai6304', 'venkatesh_chevuru', 'vijji_1408', 'vikas_gosula', 'vinay_chepuru', 'vinaycherry143', 'vishnu_teja__reddy', 'warm_walker_', 'wiz_kidoo_', 'world_of_adarsh_vikas', 'yashuyaswanth1290', 'yedukondalu3634', 'yogeeshamuluru', 'yogesh_vijay2001', 'yogeswar__reddy__']
temp_time_slot_bookings = []
admins=['a__.r_.u_.n__', 'user_not_found_x20']

student_names = {'21KB1A0301': 'ALLAM HARSHAVARDHAN', '21KB1A0302': 'ANANTANENI TEJA KIRAN',
                 '21KB1A0303': 'ARUMULLA HARSHA VARDHAN', '21KB1A0304': 'BANDILA HARSHA',
                 '21KB1A0305': 'BANDLA KARTHIK', '21KB1A0306': 'BELLAMKONDA SARATH KUMAR',
                 '21KB1A0307': 'CHAMARTHI JAYAPRASADU', '21KB1A0308': 'CHEVULA VENKATESH',
                 '21KB1A0309': 'CHITTIBOIANA VISHNU VARDHAN', '21KB1A0310': 'DUVVURU VIVEK KUMAR',
                 '21KB1A0311': 'EMBETI VIKKY', '21KB1A0312': 'GALI NITHIN', '21KB1A0313': 'GUNDUBOYINA SUMANTH',
                 '21KB1A0314': 'KOTHAPATNAM VINAY', '21KB1A0315': 'KOTURU SAKESH', '21KB1A0316': 'LOKKU CHANDRA SEKHAR',
                 '21KB1A0317': 'MEKALA SUJITH', '21KB1A0318': 'MUTHYALA SAI VIGNESH',
                 '21KB1A0319': 'NALLISETTY VENKATA SAKETH', '21KB1A0320': 'NANNAM VINOD KUMAR',
                 '21KB1A0321': 'NAVANARI POORNA CHANDRA', '21KB1A0322': 'NELLIPUDI RAHUL VARDHAN',
                 '21KB1A0323': 'NIMMALA LEELAPRADEEP', '21KB1A0324': 'NIPPATLAPALLI PRAVEEN',
                 '21KB1A0325': 'PALLAM NARASIMHULU', '21KB1A0326': 'PALUKURI LOHITH',
                 '21KB1A0327': 'PANTA VENKATA RITHWICK', '21KB1A0328': 'PERIMDESAM SIDDARDHA',
                 '21KB1A0329': 'PUDI HARIBABU', '21KB1A0330': 'PULIVARTHI GURU KRISHNA',
                 '21KB1A0331': 'PUTTA VEERA VENKATA SIVA', '21KB1A0332': 'RAJA RAMESH JEEVITH KUMAR',
                 '21KB1A0333': 'SAGUTURU SUNNY', '21KB1A0334': 'SANA YASWANTH REDDY', '21KB1A0335': 'SATHENA SESHADRI',
                 '21KB1A0336': 'SHAIK KHADAR BASHA', '21KB1A0337': 'SHAIK SANAULLA', '21KB1A0338': 'SHAIK SHAJEER',
                 '21KB1A0339': 'SYED SAAD AHAMED', '21KB1A0340': 'TEEPALAPUDI MAHESH',
                 '21KB1A0341': 'THATAMSETTY CHAITANYA', '21KB1A0342': 'THIRUMURU RAJESH',
                 '21KB1A0343': 'THIRUNAMALLI SANDEEP', '21KB1A0344': 'THONDA MUNEENDRA BABU',
                 '21KB1A0345': 'THOTA GANESH', '21KB1A0346': 'THUGUTLA CHENNA KESAVA REDDY',
                 '21KB1A0347': 'THUPILI KASTHURI BABU', '21KB1A0348': 'TURIMERLA VINAY KUMAR',
                 '21KB1A0349': 'UDAYAGIRI SIVASAI', '21KB1A0350': 'UTUKURU INDRA REDDY',
                 '21KB1A0351': 'VENDOTI BHAVESH REDDY', '21KB1A0352': 'VIJAYA SONU NIGHAM', '21KB1A0353': 'YATA BALAJI',
                 '21KB1A0501': 'AKULA SRINADH REDDY', '21KB1A0502': 'AKULA VENKATAMANOJ',
                 '21KB1A0503': 'AMBATI BHAVISHYA', '21KB1A0504': 'AMBATI PRATHIBHA',
                 '21KB1A0505': 'AMMINENI HARSHITHA', '21KB1A0506': 'ANTHATI BALAJI',
                 '21KB1A0507': 'ANUGULA THARUN CHOWDARY', '21KB1A0508': 'BANDI PAVAN KALYAN',
                 '21KB1A0509': 'BANDI POOJASRI', '21KB1A0510': 'BATHALA DHEERAJ CHOWDHARI',
                 '21KB1A0511': 'BATTA SAIVAMSI', '21KB1A0512': 'BEEDA DEVI CHANDANA',
                 '21KB1A0513': 'BELLAMKONDA HEMANJALI', '21KB1A0514': 'BELLAPU ARCHANA',
                 '21KB1A0515': 'BHUMIREDDY SUBBAREDDY', '21KB1A0516': 'BITRAGUNTA SASI KUMAR',
                 '21KB1A0517': 'BOMMI REDDY BHARATH REDDY', '21KB1A0518': 'BORIGALA PUSHPA RAJ',
                 '21KB1A0519': 'BUDANAM YASWANTHI', '21KB1A0520': 'CHALLA CHENCHUSUDHA',
                 '21KB1A0521': 'CHALLA NITHISH RAJU', '21KB1A0522': 'CHALLA SAISURAJ',
                 '21KB1A0523': 'CHAPALA NAVEEN KUMAR', '21KB1A0524': 'CHEJARLA NAVEEN',
                 '21KB1A0525': 'CHEMUKULA SUMALATHA', '21KB1A0526': 'CHITTURU SRIYA',
                 '21KB1A0527': 'DAGGOLU MUNI HARSHAVARDHAN REDDY', '21KB1A0528': 'DARA NARENDRA',
                 '21KB1A0529': 'DASARI SAI KALPANA', '21KB1A0530': 'DASEPALLI DEEPTHI',
                 '21KB1A0531': 'DESABOYINA ASHIK', '21KB1A0532': 'DEVARAKONDA DEVARSHINI',
                 '21KB1A0533': 'DEVARAYALA PRANEETH', '21KB1A0534': 'DEVISETTY SRAVANI',
                 '21KB1A0535': 'DHODDAGA YAMINI', '21KB1A0536': 'DUDDU MADHAVI',
                 '21KB1A0537': 'DUMPA MADHURI', '21KB1A0538': 'DUMPA POORNA CHANDRA REDDY',
                 '21KB1A0539': 'DUPATI GNANA PRASUNAMBIKA KUSUMANJALI', '21KB1A0540': 'DUVVURU NITHIN',
                 '21KB1A0541': 'EESA MANASA', '21KB1A0542': 'ELURU VENKATA RAMANAIAH',
                 '21KB1A0543': 'ENDLURI SANGEETHA', '21KB1A0544': 'GADAMSETTY VASAVI YOSHITHA',
                 '21KB1A0545': 'GANAPARTHI HARSHITHA', '21KB1A0546': 'GANDLA VENU',
                 '21KB1A0547': 'GANTA PAVANI', '21KB1A0548': 'GANTASALA DEEVENA KUMARI',
                 '21KB1A0549': 'GANUGAPENTA KEERTAN', '21KB1A0550': 'GARNENI VYSHNAVI',
                 '21KB1A0551': 'GOLLA LAKSHMI SRINIVAS', '21KB1A0552': 'GONA PENCHALA LAKSHMI DEVI',
                 '21KB1A0553': 'GONELA VIGNESH KUMAR', '21KB1A0554': 'GONU LAKSHMI SANJANA',
                 '21KB1A0555': 'GUDURU JASHWANTH', '21KB1A0556': 'GUJJALAPUDI HARIKA',
                 '21KB1A0557': 'GUNNAMREDDY THANMAI', '21KB1A0558': 'HARIHARAN HARINI',
                 '21KB1A0559': 'J RANJAN', '21KB1A0560': 'JAMALLA NARESH', '21KB1A0561': 'JAYAMPU VISHNU VARDHAN REDDY',
                 '21KB1A0562': 'KAKU PUNITH REDDY', '21KB1A0563': 'KALATHURU ASRITHA',
                 '21KB1A0564': 'KALLURU POOJITHA', '21KB1A0565': 'KAMATHAM LAKSHMI PRASANNA',
                 '21KB1A0566': 'KANDIKATTU DEVI SRINIVAS', '21KB1A0567': 'KANNA BHANUPRAKASH',
                 '21KB1A0568': 'KASIREDDY MANASWINI REDDY', '21KB1A0569': 'KHUSHI SHARMA',
                 '21KB1A0570': 'KOLLI DEEPTHI', '21KB1A0571': 'KOLLU SAI HARSHITHA',
                 '21KB1A0572': 'KOMARAGIRI CHANDU', '21KB1A0573': 'KOMMI NANI KAVITHA',
                 '21KB1A0574': 'KONDLAPUDI SUPREETHI', '21KB1A0575': 'KONDURU GAYATHRI',
                 '21KB1A0576': 'KONDURU GAYATHRI', '21KB1A0577': 'KONDURU KUSUMA LATHA',
                 '21KB1A0578': 'KOPPALA NITHISH KUMAR', '21KB1A0579': 'KORA NEHITHA CHOUDHARY',
                 '21KB1A0580': 'KORAPATI HARSHAVARDHAN', '21KB1A0581': 'KORAPATI SAI THRIVEDH CHOWDARY',
                 '21KB1A0582': 'KOTAPATI VENKATA LAKSHMI', '21KB1A0583': 'KOTHAPALLI SUSMITHA',
                 '21KB1A0584': 'KUDARI CHINNA SUMANTH', '21KB1A0585': 'LEBURU HARSHA NANDINI',
                 '21KB1A0586': 'LEKKALA THRISHA', '21KB1A0587': 'MADAMANCHI VANDANA',
                 '21KB1A0588': 'MADANA BALAHARINI', '21KB1A0589': 'MANGUDODDI VAMSI KRISHNA',
                 '21KB1A0590': 'MANNEMUDDU HEMAVALLI', '21KB1A0591': 'MANNURU PRUDHVI',
                 '21KB1A0592': 'MARELLA HEMANTH', '21KB1A0593': 'MARELLA HEMSASANTH',
                 '21KB1A0594': 'MATHANGI SRAVANI', '21KB1A0595': 'MEER AMEENA KULSUM',
                 '21KB1A0596': 'MOGILI VENKATA SAI THARUN', '21KB1A0597': 'MOODI NANDHINI',
                 '21KB1A0598': 'MORAMREDDY HANVITHA', '21KB1A0599': 'MOTHUKURI RAJEEV',
                 '21KB1A05A0': 'MUMMADI VENKATA SAI PRASAD', '21KB1A05A1': 'MUSTIGUNTA DEVI PRIYA',
                 '21KB1A05A2': 'MUTHYALA DHANUSH', '21KB1A05A3': 'MYLA POOJITHA',
                 '21KB1A05A4': 'NADAVALA ASRITHA', '21KB1A05A5': 'NAGAM SIVA GAYATHRI',
                 '21KB1A05A6': 'NAGISETTY DYVA ABHILASH', '21KB1A05A7': 'NAIDU MITHUNREDDY',
                 '21KB1A05A8': 'NAISA SUMANA SREE REDDY', '21KB1A05A9': 'NAMBURU HIMASWI',
                 '21KB1A05B0': 'NANDA BALAJI', '21KB1A05B1': 'NARA NELLORE GANESH',
                 '21KB1A05B2': 'NATARU SRIMOUNIKA', '21KB1A05B3': 'NATTETI UDAY KUMAR',
                 '21KB1A05B4': 'NEELAKANTAM RAHUL', '21KB1A05B5': 'NEELAM RATNAM',
                 '21KB1A05B6': 'NELABALLI GEETHANJALI', '21KB1A05B7': 'NELLORU POOJITHRI',
                 '21KB1A05B8': 'NITIN KUMAR', '21KB1A05B9': 'NOTI SRILAKSHMI', '21KB1A05C0': 'OJILI KOUSALYA',
                 '21KB1A05C1': 'PADARTHI KEERTHI', '21KB1A05C2': 'PAKUPODI SATHISH',
                 '21KB1A05C3': 'PALAGATI SAI GOWTHAM REDDY', '21KB1A05C4': 'PALAGATI SAI VARDHAN',
                 '21KB1A05C5': 'PALLAM ANUSHA', '21KB1A05C6': 'PALURI ROHITHA',
                 '21KB1A05C7': 'PAMUJULA VINEETHA', '21KB1A05C8': 'PAMULA SURENDRA',
                 '21KB1A05C9': 'PANTA SASIKANTH', '21KB1A05D0': 'PAVAN SATHWIK CVHN', '21KB1A05D1': 'PENNA LOWKYA',
                 '21KB1A05D2': 'PERAMALASETTY VIGNESH RAJA', '21KB1A05D3': 'PESALA AADARSH VIVEK',
                 '21KB1A05D4': 'PESALA MAYURI', '21KB1A05D5': 'PUNDI VENKATESWARLU', '21KB1A05D6': 'PUTTU HEMA',
                 '21KB1A05D7': 'PUTTU JEEVAN KUMAR', '21KB1A05D8': 'RACHAMALLI VISALA',
                 '21KB1A05D9': 'RAJPUTHRA GOKUL', '21KB1A05E0': 'RAMIREDDY ANURADHA',
                 '21KB1A05E1': 'RAVILLA ANUSHA', '21KB1A05E2': 'RAYAPU POOJITHA',
                 '21KB1A05E3': 'REDDY SPHARJAN', '21KB1A05E4': 'RENINGI LAKSHMI PRASANNA',
                 '21KB1A05E5': 'ROLLA DHANUSH REDDY', '21KB1A05E6': 'SAMALA LAKSHMI PRIYA',
                 '21KB1A05E7': 'SANKHAVARAPU SIREESHA', '21KB1A05E8': 'SANNIBOINA ANJALI',
                 '21KB1A05E9': 'SARASWATHI VENKATA JAYA VARDHAN', '21KB1A05F0': 'SATHIPATI KUMAR',
                 '21KB1A05F1': 'SHAIK AASHIK AHAMAD', '21KB1A05F2': 'SHAIK ALMAS AZAM',
                 '21KB1A05F3': 'SHAIK ASHIK ELAHI', '21KB1A05F4': 'SHAIK FAZILA', '21KB1A05F5': 'SHAIK JAVEED',
                 '21KB1A05F6': 'SHAIK LIFIYA', '21KB1A05F7': 'SHAIK MANEESHA', '21KB1A05F8': 'SHAIK MOHAMMAD',
                 '21KB1A05F9': 'SHAIK MOHAMMAD MUJAHEED', '21KB1A05G0': 'SHAIK NAYILA',
                 '21KB1A05G1': 'SHAIK REEHANA', '21KB1A05G2': 'SHAIK SAHERA BANU', '21KB1A05G3': 'SHAIK SAMEER',
                 '21KB1A05G4': 'SHAIK YASEEN NASEEFA', '21KB1A05G5': 'SHAIK YASIN',
                 '21KB1A05G6': 'SHAIK YESDHANI', '21KB1A05G7': 'SIDDAVARAM NANDINI',
                 '21KB1A05G8': 'SIMMAMUDI AJAY KUMAR', '21KB1A05G9': 'SOGA HEMANTH',
                 '21KB1A05H0': 'SOMISETTY VENKATA SIVA SAI SUNAYANEE',
                 '21KB1A05H1': 'SRIRAMAKAVACHAM KRISHNA TEJASWINI', '21KB1A05H2': 'SURTHANI KARTHIKEYANI',
                 '21KB1A05H3': 'SWARNA BHARATH KUMAR REDDY', '21KB1A05H4': 'SYED MASTHAN SHABANA',
                 '21KB1A05H5': 'TATAPAREDDY PRAVEEN', '21KB1A05H6': 'THANJAVOORU DIVYA',
                 '21KB1A05H7': 'THATIPARTHI SAI KIRAN', '21KB1A05H8': 'THIRUMALASETTY HARSHITHA',
                 '21KB1A05H9': 'THIRUNAMALLI RUPA SRI VARSHA', '21KB1A05I0': 'THONDALA BHARATHI',
                 '21KB1A05I1': 'THURAKA JYOTHISH', '21KB1A05I2': 'TIRUMALA SETTY KUMAR', '21KB1A05I3': 'UPPU DINESH',
                 '21KB1A05I4': 'VALLEPU MUKUNDA', '21KB1A05I5': 'VALMETI JASHWANTH REDDY',
                 '21KB1A05I6': 'VARADARAJU NIKHITHA', '21KB1A05I7': 'VAVILLA USHA',
                 '21KB1A05I8': 'VEGURU SUKUMAR', '21KB1A05I9': 'VELIKANTI HEMANTH',
                 '21KB1A05J0': 'VENKATESWARLU KISHORE', '21KB1A05J1': 'YADAPALLI GANGA SRAVYA',
                 '21KB1A05J2': 'YADAVALLI BALAJI', '21KB1A05J3': 'YADDALA RISHITHA',
                 '21KB1A05J4': 'YAKASIRI SANTHOSH', '21KB1A05J5': 'YAKASIRI VAMSI KRISHNA',
                 '21KB1A05J6': 'YANAMALA VENKATA SRAVANTHI', '21KB1A05J7': 'YENIMETI KAVYA',
                 '21KB1A05J8': 'YETURU MANASA', '21KB1A0401': 'ADIPIREDDY SUPRATHIKA',
                 '21KB1A0402': 'ALLAMPATI LAKSHMI SREE', '21KB1A0403': 'ALURU SAI MADHAV',
                 '21KB1A0404': 'AMBATI SATWIKA', '21KB1A0405': 'ANNAVARAM DIVYA',
                 '21KB1A0406': 'ARAVA YAMUNA', '21KB1A0407': 'ARUSURU CHARANSAI', '21KB1A0408': 'BADUGU NARAHARI',
                 '21KB1A0409': 'BANDI VENKATARAMANAMMA', '21KB1A0410': 'BANDI VENKATESH',
                 '21KB1A0411': 'BANDLA LEELA MANOHAR', '21KB1A0412': 'BARRELA PRAVEEN KUMAR',
                 '21KB1A0413': 'BATHALA VENKATA PALLAVI', '21KB1A0414': 'BATTA MANASA',
                 '21KB1A0415': 'BATTA SAI KRISHNA', '21KB1A0416': 'BELLAMKONDA GAYATHRI',
                 '21KB1A0417': 'BHOGINENI NAGESWARI', '21KB1A0418': 'BIRADAVOLU KAMESWARI',
                 '21KB1A0419': 'BODICHERLA JAYANTH', '21KB1A0420': 'BOJJA VENKATESWARLU',
                 '21KB1A0421': 'BYRI SUJITHA', '21KB1A0422': 'CHALAMALA MANJULA DEVI',
                 '21KB1A0423': 'CHALLA DEVA HARSHA', '21KB1A0424': 'CHALLA MOHANKRISHNA',
                 '21KB1A0425': 'CHAMARTHI JASWITHA', '21KB1A0426': 'CHEELAPOGU CHARANTEJA',
                 '21KB1A0427': 'CHEELASANI RUCHITHA', '21KB1A0428': 'CHEKKIRALA SIVA CHANDU',
                 '21KB1A0429': 'CHENI PRANEETH', '21KB1A0430': 'CHIKICHERLA VENKATA SUJITH',
                 '21KB1A0431': 'CHILAMKURI KIRAN KUMAR', '21KB1A0432': 'CHILLI PRABHU TEJA',
                 '21KB1A0433': 'CHINTHAKUNTLA MADHURI', '21KB1A0434': 'CHINTHAPUDI BADRI',
                 '21KB1A0435': 'CHITTETI ABHINAYA', '21KB1A0436': 'CHITTETI SRIKANTH',
                 '21KB1A0437': 'DAGGOLU VANDANA', '21KB1A0438': 'DAGGUPATI MADHU',
                 '21KB1A0439': 'DAMAVARAPU SUMANTH KUMAR', '21KB1A0440': 'DEGA MANJUSHA',
                 '21KB1A0441': 'DEVANDLA KEERTHI', '21KB1A0442': 'DEVAREDDY MAYURI',
                 '21KB1A0443': 'DODDAGA AJAY KUMAR', '21KB1A0444': 'DODDI SUMANTH KUMAR',
                 '21KB1A0445': 'DOLA CHANDRA MANOHAR REDDY', '21KB1A0446': 'DOSAKAYALA HARSHITHA',
                 '21KB1A0447': 'EEGA VARSHINI', '21KB1A0448': 'ERUGU SUMA', '21KB1A0449': 'GALI PREM KUMAR',
                 '21KB1A0450': 'GANDHAM GUNA SEKHAR', '21KB1A0451': 'GANDLA JASWANTH SAI KUMAR',
                 '21KB1A0452': 'GORLA MADHU BABU', '21KB1A0453': 'GORRIPATI HARITHA', '21KB1A0454': 'GOSULA VIKAS',
                 '21KB1A0455': 'GUDI KRISHNAVENI', '21KB1A0456': 'GUDURU NIKHIL',
                 '21KB1A0457': 'GUNTAGANI SANDEEP KUMAR', '21KB1A0458': 'INNAMALA KRANTHI BABU',
                 '21KB1A0459': 'IRAKAM CHANDRIKA', '21KB1A0460': 'JAKKAM NANDINI',
                 '21KB1A0461': 'JETTI VARSHINI PRIYA', '21KB1A0462': 'KADIMPATI SAI HEMANTH',
                 '21KB1A0463': 'KADIYALA DEEPTHI', '21KB1A0464': 'KAKARLA SIVA PRASAD',
                 '21KB1A0465': 'KALAHASTHI MANASA', '21KB1A0466': 'KALICHAPPIDI MAHENDRA',
                 '21KB1A0467': 'KALISETTY GURU KALYAN', '21KB1A0468': 'KANAMARLAPUDI JAHNAVI',
                 '21KB1A0469': 'KANCHARLA KRISHNA KUMAR', '21KB1A0470': 'KANDIKATTU KHUSHUWANTH',
                 '21KB1A0471': 'KANTEPALLI RAMAKRISHNA', '21KB1A0472': 'KARI VARSHITHA',
                 '21KB1A0473': 'KARIKATI HARSHA VARDHAN', '21KB1A0474': 'KARPURAPU AKSHAY',
                 '21KB1A0475': 'KARPURAPU DINESH', '21KB1A0476': 'KATARI MUNI GOWTHAM',
                 '21KB1A0477': 'KATHARI JAYENDRA MUNI', '21KB1A0478': 'KETHABOYENA SNIGDHA',
                 '21KB1A0479': 'KONDETI TEJA SRI', '21KB1A0480': 'KONDURU LOKESH',
                 '21KB1A0481': 'KONDURU SREENIJA', '21KB1A0482': 'KOTHA VENKATA SAI LIKHITH',
                 '21KB1A0483': 'KUDIRI CHAITANYA LAKSHMI', '21KB1A0484': 'MADDURI BALAJI REDDY',
                 '21KB1A0485': 'MANGANELLORE POOJITHA', '21KB1A0486': 'MANGU HEMA DEEPIKA',
                 '21KB1A0487': 'MANNARAPU VENKAT SAI MANOJ', '21KB1A0488': 'MANNI PAVANI',
                 '21KB1A0489': 'MATHYAM JASWANTH', '21KB1A0490': 'MERAGA SUMA', '21KB1A0491': 'METTU MUNI CHANDRA',
                 '21KB1A0492': 'MORA NAVYA', '21KB1A0493': 'MORLA VENKATA SURENDRA',
                 '21KB1A0494': 'MOTTREDDY MADHURI', '21KB1A0495': 'MUCHAKALA SANDEEP',
                 '21KB1A0496': 'MUTHUKURU PAVAN KUMAR', '21KB1A0497': 'NANIMELA NANDA KISHORE',
                 '21KB1A0498': 'NANNURU SRINIVASULU', '21KB1A0499': 'NASINASAI SWAPNA',
                 '21KB1A04A0': 'NEELAPAREDDY NAVANTH REDDY', '21KB1A04A1': 'NELAVALLI LAKSHMI',
                 '21KB1A04A2': 'PALAKEERTHI BALAJI', '21KB1A04A3': 'PALEM GOPAL',
                 '21KB1A04A4': 'PALLAMPARTI MAHENDRA REDDY', '21KB1A04A5': 'PALLAPOTHULA CHANUKYA',
                 '21KB1A04A6': 'PALLAPU NITHIN', '21KB1A04A7': 'PARVATHALA MOHITH',
                 '21KB1A04A8': 'PARVATHALA POOJITHA', '21KB1A04A9': 'PATAN ARSHAD KHAN',
                 '21KB1A04B0': 'PATTAPU PADMA', '21KB1A04B1': 'PATTURU VENKATA NADESH',
                 '21KB1A04B2': 'PATURU REDDY HIMAKUMAR', '21KB1A04B3': 'PELLURU NAVEEN SAI',
                 '21KB1A04B4': 'PERENNAGARI YOGESWAR', '21KB1A04B5': 'PERISETLA HARSHA',
                 '21KB1A04B6': 'PILLAKADUPU KAVERI', '21KB1A04B7': 'PODILI MANASA',
                 '21KB1A04B8': 'POLIPOGU PRATHYUSHA', '21KB1A04B9': 'POLISETTY KEERTHI',
                 '21KB1A04C0': 'PONNA MUNI PRAKASH', '21KB1A04C1': 'PUCHALAPALLI MASTHAN',
                 '21KB1A04C2': 'PUTTU MUNI BHAVANA', '21KB1A04C3': 'RAPURU SRIHARI', '21KB1A04C4': 'SANDI DINESH',
                 '21KB1A04C5': 'SANGEETHAM LOKESH', '21KB1A04C6': 'SARVISETTY KHYATHI LEKHA',
                 '21KB1A04C7': 'SHAIK ARIF', '21KB1A04C8': 'SHAIK ARSHIYA', '21KB1A04C9': 'SHAIK ASIF',
                 '21KB1A04D0': 'SHAIK AYESHA', '21KB1A04D1': 'SHAIK AYISHA', '21KB1A04D2': 'SHAIK FAIZ AHAMED',
                 '21KB1A04D3': 'SHAIK IRFAN BASHA', '21KB1A04D4': 'SHAIK ISMAIL', '21KB1A04D5': 'SHAIK JAHEERUDDIN',
                 '21KB1A04D6': 'SHAIK JASMIN HASEENA', '21KB1A04D7': 'SHAIK LALU',
                 '21KB1A04D8': 'SHAIK NOORULLA', '21KB1A04D9': 'SHAIK REEHAN', '21KB1A04E0': 'SHAIK SAMEER',
                 '21KB1A04E1': 'SHAIK SUFIYA', '21KB1A04E2': 'SHAIK THAJWIN',
                 '21KB1A04E3': 'SIRIGIRI VENKATA PRAVEEN KUMAR', '21KB1A04E4': 'SREEPATHI SUSHMA',
                 '21KB1A04E5': 'SRI PATHI VAMSI', '21KB1A04E6': 'SUNKARA GOPI', '21KB1A04E7': 'TAGARAM HABEEB',
                 '21KB1A04E8': 'TALAPALA MANJULA', '21KB1A04E9': 'THANIPARTHI TARUN TEJA',
                 '21KB1A04F0': 'THIGALA RANJITH KUMAR', '21KB1A04F1': 'THOTA HARSHITHA',
                 '21KB1A04F2': 'THUMATI VENKATADEVAKI', '21KB1A04F3': 'UPPALA MADHAN KUMAR',
                 '21KB1A04F4': 'VARALA NITHYA SANTHOSH KUMAR', '21KB1A04F5': 'VARIGONDA GOWTHAM',
                 '21KB1A04F6': 'VATAMBETI DINESH', '21KB1A04F7': 'VEDANTHAM SREELEKHA',
                 '21KB1A04F9': 'VEMULA POOJITHA', '21KB1A04G0': 'VEMULURI MADHUMITHA',
                 '21KB1A04G1': 'VETTI YOGESH', '21KB1A04G2': 'VINJAMURU VENKATA GANESH',
                 '21KB1A04G3': 'VUDAGUNDLA SHIVARANGA', '21KB1A04G4': 'YALLASIRI PREM SAI',
                 '21KB1A04G5': 'YANAMALA SUPRAJA', '21KB1A04G6': 'YARAGALA PRADEEP',
                 '21KB1A04G7': 'YARASI JAHNAVI', '21KB1A04G8': 'YARRAMATHI SYAM PRAKASH',
                 '21KB1A04G9': 'YATHAM ADI SHANKAR REDDY', '21KB1A04H0': 'YATHAM MOUNESH',
                 '21KB1A04H1': 'YEGIREDDY SIVAKUMAR', '21KB1A04H2': 'YERRANAGULA SRI NADH REDDY',
                 '21KB1A0201': 'AKULA PRANAY KUMAR', '21KB1A0202': 'ALIDENA SAHITHI',
                 '21KB1A0203': 'AMARA CHANDANA', '21KB1A0204': 'ANNABATHINA GANESH',
                 '21KB1A0205': 'ATHINA SUMALATHA', '21KB1A0206': 'BATHALA VENKATA PRIYANKA',
                 '21KB1A0207': 'BATTALA PRANATHI', '21KB1A0208': 'BUDDA BAHADEVA REDDY',
                 '21KB1A0209': 'CHAMARTHI LOKESH', '21KB1A0210': 'CHELIKAM SINDHU REDDY',
                 '21KB1A0211': 'CHENDULURU VASANTHI', '21KB1A0212': 'CHINTHAPANTI BHARGAVI',
                 '21KB1A0213': 'CHIPINAPI VAMSIKRISHNA', '21KB1A0214': 'CHIRUVELLA SURENDRA',
                 '21KB1A0215': 'DALAVAI SRUTHI', '21KB1A0216': 'DAMAYI AJAY KUMAR',
                 '21KB1A0217': 'DASARI HARI BABU', '21KB1A0218': 'DEVARAKONDA LAKSHMI SAI TEJA',
                 '21KB1A0219': 'DHURJATI VENKATA NARAYANA', '21KB1A0220': 'DODLA PAVAN',
                 '21KB1A0221': 'GANDIKOTA GOWTHAM', '21KB1A0222': 'GANGALAPUDI GAYATHRI',
                 '21KB1A0223': 'GANGAVARAPU SREELAKSHMI', '21KB1A0224': 'GANGI REDDY DIVYA DARSINI',
                 '21KB1A0225': 'GANGIREDDY SAI SANDHYA', '21KB1A0226': 'GANJI DELPHIGRACY',
                 '21KB1A0227': 'GUNJI YEDUKONDALU', '21KB1A0228': 'GUTTI BINDU', '21KB1A0229': 'GUTTI NAVANTHI',
                 '21KB1A0230': 'INGILALA HARI PAVAN', '21KB1A0231': 'INGILELA LOURDHU MARTINA MISHRA',
                 '21KB1A0232': 'JAKKALA BALAJI', '21KB1A0233': 'JITTA VAISHNAVI',
                 '21KB1A0234': 'KAKURU SAICHANDANA', '21KB1A0235': 'KAMATHAM HARSHAVARDHAN',
                 '21KB1A0236': 'KARAKAMBETI SUSHMA', '21KB1A0237': 'KATTA SIVA SANKAR',
                 '21KB1A0238': 'KATURU RAKESH', '21KB1A0239': 'KETHABOYENA ABHIGNA', '21KB1A0240': 'KOPPOLU AKASH',
                 '21KB1A0241': 'KOTA PRAVEEN', '21KB1A0242': 'KUMPATI PRAMEELA',
                 '21KB1A0243': 'KUNDURTHI VAISHNAVI', '21KB1A0244': 'MADDELA YASWANTH VENKATA KRISHNA',
                 '21KB1A0245': 'MADHURANTHAKAM PRUDHVI RAJ', '21KB1A0246': 'MALLI ADHARSH',
                 '21KB1A0247': 'MALLI SAI KUMAR', '21KB1A0248': 'MALLI SREE SAI',
                 '21KB1A0249': 'MARTHALA VENKATA RAVI TEJA', '21KB1A0250': 'MEDURU BHARATH',
                 '21KB1A0251': 'MITTATMAKURU RAMESH', '21KB1A0252': 'NAGALAPURAM MANASA',
                 '21KB1A0253': 'NALAMAKA ANU', '21KB1A0254': 'NANIMELA LAKSHMI LAHARI',
                 '21KB1A0255': 'PAKAM CHANDANA', '21KB1A0256': 'PALAKONDA HARSHA VARDHAN',
                 '21KB1A0257': 'PANTA SRAVANKUMAR REDDY', '21KB1A0258': 'PANTRANGAM SUNANDA',
                 '21KB1A0259': 'PARICHERLA SAITEJA', '21KB1A0260': 'PERUMALLA ARATHI LAKSHMI MAHESWARI',
                 '21KB1A0261': 'PERUMALLA VAISHNAVI', '21KB1A0262': 'POKKALI YOSHITHA',
                 '21KB1A0263': 'PULLURU HARI', '21KB1A0264': 'PURINI PALLAVI', '21KB1A0265': 'REGALAGUNTA SURESH',
                 '21KB1A0266': 'SAMUDRALA GAYATHRI', '21KB1A0267': 'SANIVARAPU KEERTHI REDDY',
                 '21KB1A0268': 'SHAIK ABDUL USMAN', '21KB1A0269': 'SHAIK ARSHAD', '21KB1A0270': 'SHAIK ISMAIL',
                 '21KB1A0271': 'SHAIK KHAJA HUSSAIN', '21KB1A0272': 'SHAIK NOOR MOHAMMAD', '21KB1A0273': 'SHAIK SHANNU',
                 '21KB1A0274': 'SHAIK SOHAIL', '21KB1A0275': 'SOMAVARAPU SANTHOSH', '21KB1A0276': 'SONGA SRINIVASULU',
                 '21KB1A0277': 'SUDDULA SAI SATISH', '21KB1A0278': 'TEKKEM ANANTA VENKATA NAVEEN',
                 '21KB1A0279': 'THALLURU SRIHARI', '21KB1A0280': 'THATIKONDA PREETHI',
                 '21KB1A0281': 'THATIPARTHI BUVANESH', '21KB1A0282': 'THEEPALAPUDI NAGABHUSHANA',
                 '21KB1A0283': 'ULSA MOHITH', '21KB1A0284': 'UPPALA KUSUMANJALI', '21KB1A0285': 'V HARSHAVARDHAN',
                 '21KB1A0286': 'VAKATI SUCHITRA', '21KB1A0287': 'VANJIVAKA VISPANTH',
                 '21KB1A0288': 'VEMASANI SRAVAN', '21KB1A0289': 'VENNAPUSA VIVEKANANDA REDDY',
                 '21KB1A0290': 'VUKKA SAI SWARUP', '21KB1A0291': 'VURANDURU SUPRATHIKA',
                 '21KB1A0292': 'YAKASIRI DIVYA SAI', '21KB1A0293': 'YAMBHARA CHANDU', '21KB1A0294': 'YEMBETI UJWAL',
                 '21KB1A0101': 'ADDANKI SREENADH', '21KB1A0102': 'BIJIVEMULA JASWANTH REDDY',
                 '21KB1A0103': 'CHEERA CHENCHU SASIVARDHAN', '21KB1A0104': 'CHEJERLA UDAY',
                 '21KB1A0105': 'EDURU SIREESHA', '21KB1A0106': 'EGA JASWANTHI',
                 '21KB1A0107': 'GONU ANAND KUMAR', '21KB1A0108': 'JAMGAM PRAVEEN KUMAR',
                 '21KB1A0109': 'KANNADI VENKATESH', '21KB1A0110': 'KARNA INDHU', '21KB1A0111': 'KAVALI BHAVANA',
                 '21KB1A0112': 'KAYYURU SONY', '21KB1A0113': 'KOVURU CROWN KUMAR', '21KB1A0114': 'KUMBALA JAYARAJ',
                 '21KB1A0115': 'MADAMALA UMA MAHESWARA REDDY', '21KB1A0116': 'MADHURANTHAKAM KEERTHI VASAN',
                 '21KB1A0117': 'MANDA ANIL KUMAR', '21KB1A0118': 'MARRI MAHESH', '21KB1A0119': 'MEKALA DILEEP',
                 '21KB1A0120': 'MUDDA SIDDARDHA', '21KB1A0121': 'MUPPURI PAVANKUMAR',
                 '21KB1A0122': 'NANIMELA DEVA VARAPRASAD', '21KB1A0123': 'NEELADI SRINIVASULU',
                 '21KB1A0124': 'NELLIPUDI HARSHINI', '21KB1A0125': 'PALLAVARAPU SARATH CHANDRA YADAV',
                 '21KB1A0126': 'PANCHAMURTHY ROHITH', '21KB1A0127': 'PASUMARTHI LASYASRI',
                 '21KB1A0128': 'PITLA LEELA SATHWIK', '21KB1A0129': 'PULLAGURA VINAY',
                 '21KB1A0130': 'PUTTAREDDY YESASWINI', '21KB1A0131': 'RAPURU SYAMSUNDAR REDDY',
                 '21KB1A0132': 'RUDRAPATI VENKATAPRADEEP', '21KB1A0133': 'SHAIK ILIYAZ', '21KB1A0134': 'SHAIK MAHABOOB',
                 '21KB1A0135': 'SHAIK SHAMEEL', '21KB1A0136': 'SUREDDY AKASH', '21KB1A0137': 'TUPILI KALYAN BABU',
                 '21KB1A0138': 'UDATHA PRAVEENKUMAR', '21KB1A1201': 'ATCHI ALEKHYA', '21KB1A1202': 'ATLA SISINDRI',
                 '21KB1A1203': 'BALARAJU BINDU MADHAV RAJU', '21KB1A1204': 'BANDLA LOKESH',
                 '21KB1A1205': 'BHATTARAM LALITHA MALLIKARJUNA', '21KB1A1206': 'BOLA DEEPIKA',
                 '21KB1A1207': 'BONIGALA RAJAKISHOR', '21KB1A1208': 'CHALLA PRASANTH',
                 '21KB1A1209': 'CHALLA RUCHITHA', '21KB1A1210': 'CHINTHALA HEMANTH',
                 '21KB1A1211': 'CHITTETI UDAY KUMAR', '21KB1A1212': 'DESAM LALITH KUMAR REDDY',
                 '21KB1A1213': 'DODLA HRUSHIKESH', '21KB1A1214': 'GANAMANTI VENKATA SAILAJA',
                 '21KB1A1215': 'GANGODI GANESH', '21KB1A1216': 'GOPARAJU THARUN',
                 '21KB1A1217': 'GORLA SIVA POOJITHA', '21KB1A1218': 'GURRAM SREEJA',
                 '21KB1A1219': 'K SHARIKA MADHURI', '21KB1A1220': 'KAKU PRASANNA KUMAR',
                 '21KB1A1221': 'KAMASANI RAJITHA', '21KB1A1222': 'KANNALI VEDIKA',
                 '21KB1A1223': 'KANTEPALLI VENKAT KOWSHIK', '21KB1A1224': 'KARNA YOKSHITH',
                 '21KB1A1225': 'KATARU VENKATA MURALI', '21KB1A1226': 'KATIKA MAHAMMED RAFFIQ',
                 '21KB1A1227': 'KOPPALA SASI KUMAR', '21KB1A1228': 'LAKKIREDDY GOPICHANDANA',
                 '21KB1A1229': 'MACHAVARAM MANJARI', '21KB1A1230': 'MADDELA BABI',
                 '21KB1A1231': 'MALEPATI LIKHITHA', '21KB1A1232': 'MUMMADI SIREESHA',
                 '21KB1A1233': 'MUNAGALA MADHURI', '21KB1A1234': 'NEERUPAKA MAHALAKSHMI',
                 '21KB1A1235': 'PARAKOTI DIVYA', '21KB1A1236': 'PEDDI REDDY HARINATH REDDY',
                 '21KB1A1237': 'PEDURU SAI POOJITHA', '21KB1A1238': 'PERNETI SATHVIK REDDY',
                 '21KB1A1239': 'PICHAPATI SURENDRA REDDY', '21KB1A1240': 'PODALAKURU HARINI',
                 '21KB1A1241': 'PONUGOTI JAGADEESH', '21KB1A1242': 'PRALAYA KAVERI ABHINAY KUMAR',
                 '21KB1A1243': 'RAAGIPATI PAVAN KUMAR', '21KB1A1244': 'RUDRARAJU HARSHINI',
                 '21KB1A1245': 'SAMADI KRANTHI KUMAR', '21KB1A1246': 'SHAIK HASIF',
                 '21KB1A1247': 'SHAIK MAHAMMED REHMAN', '21KB1A1248': 'YALLAMRAJU LOKESH VARMA',
                 '21KB1A3001': 'A DEEPTHI', '21KB1A3002': 'ACCHI ASHOK CHAKRAVARTHI',
                 '21KB1A3003': 'ALLAM LAHARI', '21KB1A3004': 'ARANI NIKUNJ VIHARI', '21KB1A3005': 'ARCOT YASHWANTH',
                 '21KB1A3006': 'AVULA ANUSHA', '21KB1A3007': 'BALAKRISHNA KALYAN',
                 '21KB1A3008': 'BANDI HARSHAVARDHAN', '21KB1A3009': 'BOLA SRUTHI',
                 '21KB1A3010': 'BOLIGARLA SUKUMAR', '21KB1A3011': 'CHALLA CHANDU', '21KB1A3012': 'CHALLA SAI KUMAR',
                 '21KB1A3013': 'CHAMARTHI JAHNAVI', '21KB1A3014': 'CHENNURU VINEETHA',
                 '21KB1A3015': 'CHIMMILI BHAVANA', '21KB1A3016': 'CHINNIREDDY PHANEENDRA REDDY',
                 '21KB1A3017': 'DABBUGOTTU AJAY KUMAR', '21KB1A3018': 'DONTHALA GIRIDHAR',
                 '21KB1A3019': 'DUVVURU RAJASRI', '21KB1A3020': 'DUVVURU YUGANDHAR REDDY',
                 '21KB1A3021': 'ENIMIREDDY DEVENDRA REDDY', '21KB1A3022': 'ESWARARAJU BALAJI',
                 '21KB1A3023': 'GEDI BHUVAN SAI', '21KB1A3024': 'GOLLAPALLI MITHUNA',
                 '21KB1A3025': 'GOLLAPALLI YOHAN', '21KB1A3026': 'GORTHALA SAI',
                 '21KB1A3027': 'GOWDAPERU PREM CHAKRAVARTHI', '21KB1A3028': 'GRANDHE SREE CHASWITHA',
                 '21KB1A3029': 'GUMMADISANI ANIL KUMAR REDDY', '21KB1A3030': 'GUNAPATI KAVYA',
                 '21KB1A3031': 'GUNDALA SAI KIRAN', '21KB1A3032': 'GUNJI MOUNIKA',
                 '21KB1A3033': 'GURUVINDAPUDI SREELAKSHMI', '21KB1A3035': 'JAJULA POOJITHA',
                 '21KB1A3036': 'KALAVALA LAVANYA', '21KB1A3037': 'KANDATI SUPRIYA',
                 '21KB1A3038': 'KAPULURU YUVASREE', '21KB1A3039': 'KEERTHIPATI PARITHOSH',
                 '21KB1A3040': 'KESAVARAPU JOHNSON', '21KB1A3041': 'KODURU SIVA NANDINI',
                 '21KB1A3042': 'KOLLIPARA SAI SAKETH', '21KB1A3043': 'KONIDENA VIJAY', '21KB1A3044': 'KOPPALA HEMANTH',
                 '21KB1A3045': 'KOTHURU VINAY', '21KB1A3046': 'KUMBALA CHAITANYA LAKSHMI',
                 '21KB1A3047': 'MALLEMKONDA BHARGAVA', '21KB1A3048': 'MALLU SAI CHARAN',
                 '21KB1A3049': 'MANAPATI SUJANA', '21KB1A3050': 'MANI ASWINI',
                 '21KB1A3051': 'MANNI OORMIKA', '21KB1A3052': 'MOHAMMED SAMEENA',
                 '21KB1A3053': 'MUPPALLA SAI ANKITA', '21KB1A3054': 'MURA LAZAR',
                 '21KB1A3055': 'NAGAMALLI MUNI PRAKASH', '21KB1A3056': 'NAGELLA SIREESHA',
                 '21KB1A3057': 'NAGINENI PRATHIBHA', '21KB1A3058': 'NIBBARAGANDLA RANGA DEEPTHI',
                 '21KB1A3059': 'NIMMAKAYALA SHANTHI REDDAIAH', '21KB1A3060': 'PAKINA NAGA SAILIKA',
                 '21KB1A3061': 'PALEPU LAVANYA', '21KB1A3062': 'PALLALA PRAVEEN KUMAR',
                 '21KB1A3063': 'PANCHAMURTHY VIJAYESWARI', '21KB1A3064': 'PANGANAMALA RAJESWARI MEDINI',
                 '21KB1A3065': 'PAPANA MANOHAR', '21KB1A3066': 'PAPANA PRATHIK', '21KB1A3067': 'PARICHERLA SIMHADRI',
                 '21KB1A3068': 'PASUPULETI DEVI SWETHA', '21KB1A3069': 'PATHAN ROOHI',
                 '21KB1A3070': 'PERAMSETTY KAVYASREE', '21KB1A3071': 'PETA MUNI THANUSREE',
                 '21KB1A3072': 'POKKIREDDY VAISHNAV REDDY', '21KB1A3073': 'POLURU CHAITHANYA',
                 '21KB1A3074': 'PUSALA RAGAMANASA', '21KB1A3075': 'RAVULA HARSHA VARDHAN',
                 '21KB1A3076': 'RAYAPU UDAY KUMAR', '21KB1A3077': 'SADARI JASWANTH', '21KB1A3078': 'SAMA DEVISRI',
                 '21KB1A3079': 'SANISETTY VENKATA RAJESH', '21KB1A3080': 'SARVEPALLI BHARGAV',
                 '21KB1A3081': 'SHAIK ABDULSHUKUR', '21KB1A3082': 'SHAIK IMRAN',
                 '21KB1A3083': 'SHAIK MEHARAJ BHANU', '21KB1A3084': 'SHAIK SONA',
                 '21KB1A3085': 'SHOLINGAR ABHIRAM SAI', '21KB1A3086': 'SINGAMSETTY PAVITHRA',
                 '21KB1A3087': 'SIRIGIRI BHARGAVI', '21KB1A3088': 'SURAPARAJU SAI SUSHUMNA',
                 '21KB1A3089': 'SURIPAKA SRI CHARAN', '21KB1A3090': 'THALAPANENI CHANDANA',
                 '21KB1A3091': 'THAMATAM JAYA SUSHMA', '21KB1A3092': 'TURAKA ARUNA',
                 '21KB1A3093': 'UDATHA SIVA RAJU', '21KB1A3094': 'VALLABHANENI PRATHIMA',
                 '21KB1A3095': 'VANKAYALA SRIVASAVI', '21KB1A3096': 'VATTURU SRI VARDHINI',
                 '21KB1A3097': 'VAVILI THANUJA', '21KB1A3098': 'VELU THILAGA',
                 '21KB1A3099': 'VEMANA VENKATA VARSHITH', '21KB1A30A0': 'VEMANABOINA VIKRAM',
                 '21KB1A30A1': 'VEMULA GUNA SEKHAR', '21KB1A30A2': 'Y SAMSON',
                 '21KB1A30A3': 'YARAM VENKATA DEVA SAINADH', '20KB1A1201': 'AKKEM SANTHOSH',
                 '20KB1A1202': 'ANJURU SUMAN', '20KB1A1203': 'ATLA JOSHITHA ', '20KB1A1204': 'AVULA VENKATA SAI',
                 '20KB1A1205': 'AVULA VIJAYA LAKSHMI ', '20KB1A1206': 'BANDILI SRILATHA ',
                 '20KB1A1207': 'BOMMIREDDY SAKETH REDDY', '20KB1A1208': 'BORUGADDA SAI TEJA',
                 '20KB1A1209': 'CHADALAWADA SIVA VASTHA', '20KB1A1210': 'CHILAMATHURU ABISHEK',
                 '20KB1A1211': 'DANAM AMRUTHA VARSHINI ', '20KB1A1212': 'DARUVURU ROSHINI ',
                 '20KB1A1213': 'DEVARAPALLI DEEPTHI ', '20KB1A1214': 'DEVIREDDY SOWMITHA ',
                 '20KB1A1216': 'DUVVURU ROSHINI ', '20KB1A1217': 'ETHAMUKKALA MOUNIKA ',
                 '20KB1A1218': 'GADAMSETTI DHAKSHAYANI ', '20KB1A1219': 'GALLA RICKSON', '20KB1A1220': 'GORLA REVANTH',
                 '20KB1A1221': 'GUNDALA DEEPTHIMAYI ', '20KB1A1222': 'INDURI ANISH', '20KB1A1224': 'KALE PAVAN KUMAR',
                 '20KB1A1225': 'KALLURU JAHNAVI ', '20KB1A1226': 'KALLURU KAMAL SAI NATH REDDY',
                 '20KB1A1227': 'KAPIREDDY THUMAL REDDY', '20KB1A1228': 'KEERTHIPATI MAHIDHAR',
                 '20KB1A1229': 'KETHU KAVYA ', '20KB1A1230': 'KOLLAPUDI VENKATESWARLU', '20KB1A1231': 'KUCHI BHAVANA ',
                 '20KB1A1232': 'LAYA ANKI REDDY ', '20KB1A1233': 'MADDALI SRINIVAS SATHVIK',
                 '20KB1A1234': 'MALEPATI YAMINI ', '20KB1A1235': 'MALLELA JOSHVARDHAN',
                 '20KB1A1236': 'MANGALA VENKATA KALYAN', '20KB1A1237': 'MARUBOINA CHARISHMA ',
                 '20KB1A1238': 'MUNGARA GEETHIKA ', '20KB1A1239': 'NAGIREDDY HITHOSHINI ',
                 '20KB1A1240': 'NALAMAKALA VIJITHA ', '20KB1A1241': 'NALLAPANENI JASWANTHKUMAR',
                 '20KB1A1242': 'NARAYANA SUDEEPTHI ', '20KB1A1243': 'NIMATHAM VENNELA ',
                 '20KB1A1244': 'PALLAMALA RISHITHA ', '20KB1A1245': 'PETA HEMANTH KUMAR',
                 '20KB1A1246': 'PULAKANTI SEKHAR', '20KB1A1247': 'ROKKAM PRATYUSHA ', '20KB1A1248': 'SANATHI UNNATHI ',
                 '20KB1A1249': 'SHAIK ASIF', '20KB1A1250': 'SHAIK KARISHMA ', '20KB1A1251': 'SRIRAM GEETHIKA PRIYA ',
                 '20KB1A1252': 'THOTA JAYANTH', '20KB1A1253': 'THUMMALA MANVITHA ',
                 '20KB1A1254': 'TIRUKALA PAVAN KALYAN', '20KB1A1255': 'UDATHA PAVANKUMAR',
                 '20KB1A1256': 'VALLAMETI MURALIDHAR', '20KB1A1257': 'VELURU HEMA SAITHA ',
                 '20KB1A1258': 'VEMANA RITHWIK', '20KB1A1259': 'VENNAPUSA NITHIN KUMAR REDDY',
                 '20KB1A1260': 'VENNAPUSA SIVA KUMAR', '20KB1A1261': 'YALLAMPATI RAVI',
                 '20KB1A1262': 'YARRAM REDDY GANESH REDDY', '20KB1A1215': 'DUVVURU ABHISHEK',
                 '21KB5A1201': 'CHALLA SIVA LOHITH', '21KB5A1202': 'ARAVAPALLI NAGANJANEYULU',
                 '21KB5A1203': 'CHIKOLU SIVASANKAR', '21KB5A1204': 'NALLAPANENI VENKATA KRISHNA',
                 '21KB5A1205': 'NEMBI JAGADEESH', '21KB5A1206': 'ANNA RAVI TEJA', '20KB1A3001': 'ADASANAPALLI DIVAKAR',
                 '20KB1A3002': 'ADISHTI GOWTHAM', '20KB1A3003': 'AMBAVARAPU DIVYA ',
                 '20KB1A3004': 'ANNAMETI SRAVAN KUMAR', '20KB1A3005': 'ATMAKURU NITHIN',
                 '20KB1A3007': 'BUDATHATI RAHUL', '20KB1A3008': 'CHALLA NIHARIKA ', '20KB1A3009': 'CHEMBETI JAGADEESH',
                 '20KB1A3010': 'DADDOLU PRAVEEN', '20KB1A3011': 'DASARI JAYACHANDRA', '20KB1A3012': 'GOTTIPROLU SAKETH',
                 '20KB1A3013': 'GUNDUBOINA KAVYA ', '20KB1A3014': 'JADA SUNIL', '20KB1A3015': 'KAKANI FINNY DANIEL',
                 '20KB1A3016': 'KALYANI AASRITHVATHSAL', '20KB1A3017': 'KANAPARTHYSYAM SAROJ KUMAR',
                 '20KB1A3018': 'KODAVALURU PALLAVI ', '20KB1A3019': 'KONDURU VENKATA SAI DHANUSH KUMAR',
                 '20KB1A3020': 'KUCHI RAVI KIRAN', '20KB1A3021': 'KUDITHIPUDI VIDHYA CHOWDARY ',
                 '20KB1A3022': 'LEBURU NAGENDRA BABU', '20KB1A3023': 'MALLEMKONDA SUJANA ',
                 '20KB1A3024': 'MARTHALA MONICA ', '20KB1A3025': 'MONGAN SHAIK KHOUSAR ABBOSS',
                 '20KB1A3026': 'MOODI PAVAN KUMAR', '20KB1A3027': 'MORLA HEMALATHA ', '20KB1A3028': 'MULA SIVA REDDY',
                 '20KB1A3029': 'NARABOYINA PAVAN KUMAR', '20KB1A3030': 'NETTEM DHATRISH CHOWDARY',
                 '20KB1A3031': 'PADAVALA PUSHKAR', '20KB1A3032': 'PADIGINATI BHARATH', '20KB1A3033': 'PAKALA AKHILA ',
                 '20KB1A3034': 'PANDLURU YUVARAJ', '20KB1A3035': 'PAPANA SUBBARATHNAMMA ',
                 '20KB1A3036': 'PARVATHALA ANKITHA ', '20KB1A3037': 'PATHI SRI SAKETH',
                 '20KB1A3038': 'PATHIPATI GNANA DIVYANTH', '20KB1A3039': 'PELURU RAJENDRA KUMAR REDDY',
                 '20KB1A3040': 'PESALA SUSHMITHA ', '20KB1A3041': 'PONDURU AKHILESH', '20KB1A3042': 'PULLA MADHURIMA ',
                 '20KB1A3043': 'PULLURU GANESH GURAPPAN', '20KB1A3044': 'PUNURU DHEERAJ REDDY',
                 '20KB1A3045': 'RUDRAVARAM SUDHEER', '20KB1A3046': 'SANNEBOINA AKHIL',
                 '20KB1A3047': 'SANNIBOYINA ABHIRAM', '20KB1A3048': 'SATU MADHULIKA ', '20KB1A3049': 'SHAIK JASMINE ',
                 '20KB1A3050': 'SHAIK ROSHNI ', '20KB1A3051': 'SIDDAMURTHI VENKATA SURYANARAYANA REDDY',
                 '20KB1A3052': 'SIDDILINGAM SUREKHA ', '20KB1A3053': 'SOMAVARAPU SAIKUMAR REDDY',
                 '20KB1A3054': 'SYED HAZIQ NAWAZ', '20KB1A3055': 'SYED LIYAZ', '20KB1A3056': 'TAMMI LOKESH',
                 '20KB1A3057': 'THATIPARTHI LOKESH REDDY', '20KB1A3058': 'THEEPALAPUDI PRASANTH',
                 '20KB1A3059': 'THOTLAKKAGARI DINAKAR', '20KB1A3060': 'VALLURU VENKATA SAI LEKHYA ',
                 '20KB1A3061': 'VELURU GEETHA JAYANTH CHOWDARY', '20KB1A3062': 'VISWANADHAPALLI DIVYA ',
                 '20KB1A3063': 'VUNNAM SANDEEP', '20KB1A3064': 'YANAMALA VENKATA PRASANTH REDDY',
                 '21KB5A3001': 'PATTAN ZAHEER AHMED', '21KB5A3002': 'SHAIK SHAHID AFRIDI',
                 '21KB5A3003': 'SUNAKAM VENKATARAMANA', '21KB5A3004': 'SHAIK AJMAD',
                 '21KB5A3005': 'RAMISETTY VIDYA SAGAR', '21KB5A3006': 'MADALA VENGABABU',
                 '20KB1A0301': 'AKULA NAGARAJU', '20KB1A0302': 'ALATHURU NAGA SAI', '20KB1A0303': 'AMASA BHANU PRAKASH',
                 '20KB1A0304': 'AMULURU YOGEESH SAI', '20KB1A0305': 'ANNANGI HEMANTH KUMAR',
                 '20KB1A0306': 'ARURU CHANDRA SEKHAR', '20KB1A0307': 'AVULA HEMANTH', '20KB1A0308': 'BALLEM SIVA KUMAR',
                 '20KB1A0309': 'BALLI ADARSH', '20KB1A0310': 'BANDARU MAHESH', '20KB1A0311': 'BANDI VENKATA PRASANTH',
                 '20KB1A0312': 'BANDI VENKATESWARLU', '20KB1A0313': 'BANKAPURI MANOGNA TEJA',
                 '20KB1A0314': 'BATHALA DHANUNJAYA', '20KB1A0315': 'BATTA SHANMUKH',
                 '20KB1A0316': 'BATTURI VAMSI KRISHNA', '20KB1A0317': 'BEJAWADA SIVA SAI',
                 '20KB1A0318': 'BODAGALA PENCHALA PRASAD', '20KB1A0319': 'BOMMU RAHUL REDDY',
                 '20KB1A0320': 'BUSIREDDY SURENDRA REDDY', '20KB1A0321': 'CHALLA DEVENDRA',
                 '20KB1A0322': 'CHALLA SUJITH', '20KB1A0323': 'CHALLA VENU', '20KB1A0324': 'CHANDRA VENKATA BHANU TEJA',
                 '20KB1A0325': 'CHEEKAVOLU SURESH', '20KB1A0326': 'CHEEKOLU KARTHIK',
                 '20KB1A0327': 'CHEREDDY VIJAY KUMAR', '20KB1A0328': 'CHEVURU MUNI YASWANTH KUMAR',
                 '20KB1A0329': 'CHILLAMATHURU PRUDHVI', '20KB1A0330': 'CHINTALA DHANUSH',
                 '20KB1A0331': 'CHINTHALAPUDI NAGARAJU', '20KB1A0332': 'CHINTHALAPUDI ROHITH',
                 '20KB1A0333': 'CHITTETI SAI KUMAR', '20KB1A0334': 'CHITTETI SIVA SUBRAMANYAM',
                 '20KB1A0335': 'CHITTETI VAMSI', '20KB1A0336': 'CHITTETI YASWANTH', '20KB1A0337': 'DAMARAPU PRADEEP',
                 '20KB1A0338': 'DANAM ADARSH VIKAS', '20KB1A0339': 'DARA AJAY KUMAR',
                 '20KB1A0340': 'DODDAGA CHAITANYA VARDHAN', '20KB1A0342': 'DUMPALA KRISHNAVAMSI',
                 '20KB1A0343': 'GATOLA GUNASEKHAR', '20KB1A0344': 'GUDI MUNI KOTESWARA RAO',
                 '20KB1A0345': 'GUNDU LOKESH', '20KB1A0346': 'GUNTA DHANUNJAI', '20KB1A0347': 'GUVVALA VENKATA SURESH',
                 '20KB1A0348': 'IRUKU SUMANTH', '20KB1A0349': 'JADAPALLI VENKATESWARLU',
                 '20KB1A0350': 'JAKKALA VASU RAM', '20KB1A0351': 'JANGITI GIRI', '20KB1A0352': 'JOGI BALAJI',
                 '20KB1A0353': 'JORIGE DHANUMJAY', '20KB1A0354': 'KALISETTY VENKATA CHARAN',
                 '20KB1A0355': 'KANCHARLA JYOTHI PRANEETH', '20KB1A0356': 'KANDULA BHANU CHAND',
                 '20KB1A0357': 'KANNALI MAHESH', '20KB1A0358': 'KAYYALA CHAKRAPANI',
                 '20KB1A0359': 'KONDAPURAM BRAMHA LOKESH', '20KB1A0360': 'KONIGETI GURU CHARAN',
                 '20KB1A0361': 'MACHA HARSHA VARDHAN', '20KB1A0362': 'MALLI CHAITHANYA', '20KB1A0363': 'MANDALA SRAVAN',
                 '20KB1A0364': 'MANNE ANIL KUMAR', '20KB1A0501': 'AKKURTHI SRINU', '20KB1A0502': 'ANAM PRANEETHA ',
                 '20KB1A0503': 'AUDIPUDI LOHITH KUMAR REDDY', '20KB1A0504': 'BALU PAVAN TEJA',
                 '20KB1A0505': 'BALU SRIVIDYA ', '20KB1A0506': 'BANA MANASA ', '20KB1A0507': 'BANDI ANUSHA ',
                 '20KB1A0508': 'BANDIKARLA ABHINAY SATHVIK', '20KB1A0509': 'BATHALA BALAJI',
                 '20KB1A0510': 'BHEEMAVARAPU DEVI PRIYA ', '20KB1A0511': 'BODIPEDDA LIKHITHA BLESSY ',
                 '20KB1A0512': 'BOGGULA SURYA PRAKASH REDDY', '20KB1A0513': 'BOLIGARLA PAVAN ADITHYA',
                 '20KB1A0514': 'BOLLU MAHESH', '20KB1A0515': 'BOMMISETTY PRIYATHAM TARAK',
                 '20KB1A0516': 'BOTHSA SUVARNA ', '20KB1A0517': 'CHAINRAJ NAMARATHA JAIN ',
                 '20KB1A0518': 'CHAMARTHI YASESWINI ', '20KB1A0519': 'CHANDRAGIRI SAI VARSHITHA ',
                 '20KB1A0520': 'CHEMBETI AKASH', '20KB1A0521': 'CHENNURU SAI GOWTHAM',
                 '20KB1A0522': 'CHENNURU SASI KIRAN REDDY', '20KB1A0523': 'CHEVURU MOUNIKA ',
                 '20KB1A0524': 'CHINTHA NEERAJA ', '20KB1A0525': 'CHITITHOTI HARIKRISHNA',
                 '20KB1A0526': 'CHITRA SAI KUMAR', '20KB1A0527': 'CHOPPARA RENUKA ', '20KB1A0528': 'CHUNDI DAMAN REDDY',
                 '20KB1A0529': 'DANDOLU NIKITH REDDY', '20KB1A0530': 'DEVANDLA TEJA',
                 '20KB1A0531': 'DEVARINTI SUMANTH REDDY', '20KB1A0532': 'DHANDU PRANAY TEJA',
                 '20KB1A0533': 'DODDAMREDDY VAMSI KRISHNA REDDY', '20KB1A0534': 'DONIPARTHI HEMANANDINI ',
                 '20KB1A0535': 'DONTIREDDY ACHYUTH', '20KB1A0536': 'DUVVURU SIVA RAGHAVA',
                 '20KB1A0537': 'DWARAMPUDI YOGISH REDDY', '20KB1A0538': 'EDIGA BHARATH KUMAR',
                 '20KB1A0539': 'EDURU SUNEETHA ', '20KB1A0540': 'ERRASANI BHARGAV',
                 '20KB1A0541': 'GANGAVARAPU THEJASWINI ', '20KB1A0542': 'GANGIREDDY VINEETHA ',
                 '20KB1A0543': 'GOSE PRAVEEN', '20KB1A0544': 'GUDLURU YASHWANTH',
                 '20KB1A0545': 'GUNDU CHANDHANA PRIYA ', '20KB1A0546': 'HARIPRASAD DUVVURU',
                 '20KB1A0547': 'JAGABATHINA SIDDARDA GOWTHAM', '20KB1A0548': 'JAKKALA UMA MAHESH',
                 '20KB1A0549': 'JENNIBOINA RAVEENDRA', '20KB1A0550': 'K RISHIKA MADHURI ',
                 '20KB1A0551': 'KADIMI SAI PRAGNA ', '20KB1A0552': 'KAITHAPALLI VAMSI',
                 '20KB1A0553': 'KALPAM LAKSHMI SAI PRIYA VANDANA ', '20KB1A0554': 'KANNALI HARSHA VARDHAN REDDY',
                 '20KB1A0555': 'KAPPERA RUCHITHA ', '20KB1A0556': 'KARADI SNEHITHA ',
                 '20KB1A0557': 'KARUDUMPALA SUPRAJA ', '20KB1A0558': 'KATHI AJITH GOWTHAM',
                 '20KB1A0559': 'KETHA JAYA SINDHURA ', '20KB1A0560': 'KHATEEB SHAIK AFTAB ALI',
                 '20KB1A0561': 'KOLATI VENKATA PRAVEEN KUMAR', '20KB1A0562': 'KONDA KARTHIK MANIKANTA REDDY',
                 '20KB1A0563': 'KONDREDDY KIRAN', '20KB1A0564': 'KONDURU CHANIKYA',
                 '21KB5A0501': 'BITRAGUNTA VAMSI KRISHNA', '21KB5A0502': 'GUNDUBOINA SUNEEL',
                 '21KB5A0503': 'CHALLAGUNDLA VENKATA SAI VARSHINI ', '21KB5A0504': 'SHAIK AYEESHA ',
                 '21KB5A0505': 'SHAIK APSAR ', '21KB5A0506': 'KALICHETI SATHISH BABU', '20KB1A0401': 'AABOTHULA JONESH',
                 '20KB1A0402': 'ACCHI VENKATA RATHNAIAH', '20KB1A0403': 'ADAPALA BHUVANA PRIYA ',
                 '20KB1A0404': 'ADEPPAGARI AJAY KUMAR', '20KB1A0405': 'AKELLA PHANI ADITYA',
                 '20KB1A0406': 'AMULURU DHEERAJ KUMAR', '20KB1A0407': 'ANNAMETI VASUNDHARA ',
                 '20KB1A0408': 'ARAVA DURGA VARAPRASAD', '20KB1A0409': 'ATHIKAYALA HARSHITHA ',
                 '20KB1A0410': 'ATLA VENKATA DEEPTHI ', '20KB1A0411': 'AVULA PAVITHRA ',
                 '20KB1A0412': 'AVULA YERRAMREDDYGARI BALA GANGI REDDY', '20KB1A0413': 'BADUGU KIREETI',
                 '20KB1A0414': 'BANDI VASRUTHA ', '20KB1A0415': 'BASAVARAJU VENKATA SNEHALATHA ',
                 '20KB1A0416': 'BATTA GIREESH KUMAR', '20KB1A0417': 'BATTA VINAY KUMAR',
                 '20KB1A0418': 'BATTINA SUMANTH REDDY', '20KB1A0419': 'BEERAKA LALITH KISHORE',
                 '20KB1A0420': 'BEERAKAYULU KAVITHA ', '20KB1A0421': 'BHUVANAGIRI SUMANTH',
                 '20KB1A0422': 'BODDU NANI PRASAD', '20KB1A0423': 'BOGA SAI SRINIVAS',
                 '20KB1A0424': 'BOMMISETTY VENKATA SNEHA SREE ', '20KB1A0425': 'BUDAMAGUNTA JATHIN',
                 '20KB1A0426': 'CHALLA PARAMESWARI ', '20KB1A0427': 'CHALLA SAI SATWIK',
                 '20KB1A0428': 'CHALLA SRINIVAS', '20KB1A0429': 'CHALLA YASWANTH',
                 '20KB1A0430': 'CHEEKARIPALLI ANUSHA ', '20KB1A0431': 'CHEEKAVOLU MUNISEKHAR',
                 '20KB1A0432': 'CHILLAKURU SIVANI ', '20KB1A0433': 'CHINTAKANI SUSHMA ',
                 '20KB1A0434': 'CHITTETI REVANTH', '20KB1A0435': 'CHITTETI SATYAPRIYA ',
                 '20KB1A0436': 'CHITTETI SRIKARTHIK', '20KB1A0437': 'DANDOLU LAHARI ',
                 '20KB1A0438': 'DARA PANENDRA KUMAR', '20KB1A0439': 'DARA VENU', '20KB1A0440': 'DARAPANENI CHAITHANYA',
                 '20KB1A0441': 'DESIREDDY BAVITHA ', '20KB1A0442': 'DEVABATHINA SUHITA CHOWDHARY ',
                 '20KB1A0443': 'DEVARAPALLI SWETHA ', '20KB1A0444': 'DHARMAIAHGARI VENKAT CHETHAN',
                 '20KB1A0445': 'ENAMALA HARSHITH', '20KB1A0446': 'ENDOTI SAHITHI ', '20KB1A0447': 'GADDAM MUNIKUMAR',
                 '20KB1A0448': 'GEDDAM GOWTHAMI ', '20KB1A0449': 'GOTTIPOLU PARDHAVI ', '20KB1A0450': 'GUMMA LOKESH',
                 '20KB1A0451': 'GUNDALA KEERTHI ', '20KB1A0452': 'GUNJI YASWANTH', '20KB1A0453': 'GUNJI YUVA KUMAR',
                 '20KB1A0454': 'GURRAM NIRANJANSARMA', '20KB1A0455': 'INTURU SASIDHAR',
                 '20KB1A0456': 'JAMALLA RAJ KUMAR', '20KB1A0457': 'KADIVETI HARI KISHAN', '20KB1A0458': 'KAKURU LOKESH',
                 '20KB1A0459': 'KAKURU VIJAYKRISHNA', '20KB1A0460': 'KALIKIRI CHANDU',
                 '20KB1A0461': 'KANDANURU SASI HARIKA ', '20KB1A0462': 'KANNA SHANMUKHA RAMKI',
                 '20KB1A0463': 'KAPIREDDY VYSHNAVI ', '20KB1A0464': 'KAPPA VINAY',
                 '21KB5A0401': 'TANGUTURU VENKATA KOWSHIK', '21KB5A0402': 'YASHASWINI DEGA ',
                 '21KB5A0403': 'PITCHIKA VISHNU VARDHAN BABU', '21KB5A0404': 'MUNGAMURU SRILAKSHMI ',
                 '21KB5A0405': 'NEELI SINDHU PRIYA ', '21KB5A0406': 'KOMMURU RUCHITHA ',
                 '20KB1A0201': 'ADIPIREDDY SRIKANTH', '20KB1A0202': 'ARIBOYINA MUNIKRISHNA',
                 '20KB1A0203': 'ARURU DEDEEPYA ', '20KB1A0204': 'ARUSURU SUREKHA ', '20KB1A0205': 'ATHMAKURU JYOTHI ',
                 '20KB1A0206': 'BANDILA REVANTH', '20KB1A0207': 'BHAVANASI SAI VARDHAN',
                 '20KB1A0208': 'BOLLAVARAM SATHWIKA REDDY ', '20KB1A0209': 'BOYALLA GNANA AKSHITHA ',
                 '20KB1A0210': 'CHEERA GURUTEJA', '20KB1A0211': 'CHERUVU AMRUTHA ',
                 '20KB1A0212': 'CHINTHALA BHARATH VIJAY', '20KB1A0213': 'CHINTHAMREDDY MAHITHA ',
                 '20KB1A0214': 'DAGGOLU DIVYA JYOTHI ', '20KB1A0215': 'DASARI SAI DHEEKSHITHA ',
                 '20KB1A0216': 'DHANYASI VENKATA VASANTH', '20KB1A0217': 'DINTAKURTHI HARSHADEEP',
                 '20KB1A0218': 'DORAGALLA CHANDU', '20KB1A0219': 'DUDDA SRIVARDHANREDDY',
                 '20KB1A0220': 'DUVVURU SUJITH', '20KB1A0221': 'ENGILALA NIKHILESH ADITHYA',
                 '20KB1A0222': 'GANDAVARAM SRI SIRI ', '20KB1A0223': 'GOLLAPALLI PAVANI ',
                 '20KB1A0224': 'GUNNAM PAVAN KALYAN REDDY', '20KB1A0225': 'GURRAM NIHARIKA ',
                 '20KB1A0226': 'GURUVINDAPUDI SUDARSHAN', '20KB1A0227': 'INGILELA SANGHARSH',
                 '20KB1A0228': 'JANGITI SUJITHA ', '20KB1A0229': 'JOGI SAMPATH KUMAR',
                 '20KB1A0230': 'JUVVALAPATI LEELA SAGAR', '20KB1A0231': 'KANNEBOINA UDAY CHANDRA',
                 '20KB1A0232': 'KAPULURU ANVITHA ', '20KB1A0233': 'KARAKOLLU KIRANKUMAR',
                 '20KB1A0234': 'KARNATI PAVAN KUMAR REDDY', '20KB1A0235': 'KAVALIREDDY TEJASWINI ',
                 '20KB1A0236': 'KOLLAPUDI LEELAVATHI ', '20KB1A0237': 'KOLLU SAI VINUSHNA ',
                 '20KB1A0238': 'KOLLU YAKSHITHA ', '20KB1A0239': 'KONDRAGUNTA TEJODAY',
                 '20KB1A0240': 'KONDURU SUCHAKRIDHAR REDDY', '20KB1A0241': 'KOVVURU SAI PALLAVI ',
                 '20KB1A0242': 'MANGALAPURI SAITEJA', '20KB1A0243': 'MANIKYAM RAVI TEJA',
                 '20KB1A0244': 'MANNEPALLI SOWMYA ', '20KB1A0245': 'MIRIYALA DURGA PRIYA ',
                 '21KB5A0201': 'GUMMIDIPUDI SAIVARDHAN', '21KB5A0202': 'SHAIK FAYAZ BASHA',
                 '21KB5A0203': 'VINNAKOTA KAVERI ', '21KB5A0204': 'THALLURU VICTOR BABU',
                 '21KB5A0205': 'GUNDALA BHARADWAZ', '21KB5A0206': 'MALLAM PRANEETH',
                 '21KB5A0207': 'RUDHRARAJU CHANIKYA RAJU', '21KB5A0208': 'PALOJI YESWANTH KUMAR',
                 '21KB5A0209': 'GATTU PRUDHVI LAXMAN', '21KB5A0210': 'DHURJATI VENKATA SIVA SAI SRIRAM',
                 '21KB5A0211': 'ASAM SASI KUMAR', '20KB1A0101': 'ANJURI KUSHVEE SREE ',
                 '20KB1A0102': 'APPINA VENKATA SHARAN', '20KB1A0103': 'BATTA SUKUMAR', '20KB1A0104': 'BOTULA RAVITEJA',
                 '20KB1A0105': 'CHEEPINETI ADITHYA SAI', '20KB1A0106': 'CHILAMATHURU LOKESH',
                 '20KB1A0107': 'CHITTETI UDAYKUMAR', '20KB1A0108': 'DADE ASIF KHAN',
                 '20KB1A0109': 'DEEPAGA PENCHALA PRASAD', '20KB1A0110': 'DHAKKA AJAY', '20KB1A0111': 'DURU VIVEK',
                 '20KB1A0112': 'DUVVURU SYAM SUNDAR', '20KB1A0113': 'EGA SAKETH', '20KB1A0114': 'ENDOTI SURAJ',
                 '20KB1A0115': 'GADDAM SAI CHAKRISH REDDY', '20KB1A0116': 'GANGAVARAPU MADHAN MOHAN REDDY',
                 '20KB1A0117': 'GODASU HEMASAGAR', '20KB1A0118': 'GONUGUNTA SASIDHAR',
                 '20KB1A0119': 'JAMPANA THARUN KUMAR', '20KB1A0120': 'KADANOOTHALA SAI MOUNIKA ',
                 '20KB1A0121': 'KALLURU CHENCHU JAYASIMHA REDDY', '20KB1A0122': 'KALVA PAVAN KUMAR',
                 '20KB1A0123': 'KASA SUBBA RAYULU', '20KB1A0124': 'KAVETI YASHWANTH YADAV',
                 '20KB1A0125': 'KONDAPURAM CHANDU', '20KB1A0126': 'KOTHIPAKA KALYAN SAI',
                 '20KB1A0127': 'KUDIRI SRIKARBABU', '20KB1A0128': 'LAKKU SAVYASACHITH REDDY',
                 '20KB1A0129': 'MAKKE MANASA ', '20KB1A0130': 'MANAM VENKATA AKHIL KUMAR',
                 '20KB1A0131': 'MANDA SUMANTH', '20KB1A0132': 'MANNARAPU MANUTEJA', '20KB1A0133': 'MASU MADHU',
                 '20KB1A0134': 'MATAM CHINNA SUBBARAYUDU', '20KB1A0135': 'MATTIGUNTA TEJA',
                 '20KB1A0136': 'MEDANKI JOHN WESLY', '20KB1A0137': 'MENDRAGUTHI VISHNU',
                 '20KB1A0138': 'MERAGA KASTURAIAH', '20KB1A0139': 'MUDDAM SUBBA KRISHNA',
                 '20KB1A0140': 'MUMMAREDDY YOGENDRA', '21KB5A0101': 'POTTURI MRUDULA ',
                 '21KB5A0102': 'KATURU JAYAKRISHNA', '21KB5A0103': 'POTHAMSETTY SOWDAYAN DATTA',
                 '21KB5A0104': 'VELURU BALAJI', '21KB5A0105': 'CHATLA JASMITHA ', '21KB5A0106': 'NANNEBOINA VENGAIAH',
                 '21KB5A0107': 'SIDDULUGARI SRIDHAR REDDY', '21KB5A0108': 'PUTTA GUNASEKHAR',
                 '21KB5A0109': 'P UDAY KUMAR', '21KB5A0110': 'SHAIK NOWZIL', '21KB5A0111': 'YATAGIRI SURYA PRAKASH',
                 '21KB5A0112': 'YALAVADI MOHAMMAD SOHAIL', '21KB5A0113': 'SHAIK ABDULKALAM',
                 '21KB5A0114': 'UMMADIPOLU VENKATA NAVEEN', '20KB1A0365': 'MANNE SAI', '20KB1A0366': 'MARUBOINA VAMSI',
                 '20KB1A0367': 'MEKALA HEMANTH', '20KB1A0368': 'MERIGAPUDI VENKATA PERAIAH',
                 '20KB1A0369': 'MOHAMMAD HANIFUDDIN', '20KB1A0370': 'MOHAMMED SAJID HUSSAIN',
                 '20KB1A0371': 'MUCHAKAYALA HEMANTH', '20KB1A0372': 'MUDURU JASWANTH',
                 '20KB1A0373': 'NAKKANAM VIJAY KUMAR', '20KB1A0374': 'NALAGATLA VIJAY VARDHAN REDDY',
                 '20KB1A0375': 'NALLABOTHULA VENKATA GOVARDHAN', '20KB1A0376': 'NARANELLORE VISHNU VARDHAN',
                 '20KB1A0377': 'NELLORE SREEKANTH', '20KB1A0378': 'OTTIKAYALA VEERA SANKAR',
                 '20KB1A0379': 'PALA HIMA VENKATA VARDHAN', '20KB1A0380': 'PALLEM CHAITANYA REDDY',
                 '20KB1A0381': 'PANCHETI LAKSHMIDINESH', '20KB1A0382': 'PANNURU CHARAN REDDY',
                 '20KB1A0383': 'PANNURU DHANUSH', '20KB1A0384': 'PARA JASWANTH', '20KB1A0385': 'PATNAM SUMANTH',
                 '20KB1A0386': 'PICHAPATI RAMA KRISHNA REDDY', '20KB1A0387': 'PITTI HEMANTHA KUMAR',
                 '20KB1A0388': 'PODAVAKAM NITHIN', '20KB1A0389': 'POTHALA VENKATA SHIVA', '20KB1A0390': 'PUDI RAMESH',
                 '20KB1A0391': 'PULLURU MADHU SUDHAN REDDY', '20KB1A0392': 'PULLURU SAI MANOJ',
                 '20KB1A0393': 'PUNAM MANOJ KUMAR', '20KB1A0394': 'PUTTA PRANEETH CHARAN',
                 '20KB1A0395': 'PUTTAMANENI KRISHNA SAI', '20KB1A0396': 'ROYYALA NAVEEN',
                 '20KB1A0397': 'RUPANAGUDI ANIF BASHA', '20KB1A0398': 'SANNAPUREDDY CHANDRASEKHAR REDDY',
                 '20KB1A0399': 'SHAIK ARSHAD AHMAD', '20KB1A03A0': 'SHAIK ASIEF', '20KB1A03A1': 'SHAIK KHALID ROSHAN',
                 '20KB1A03A2': 'SHAIK MASTHAN BABU', '20KB1A03A3': 'SHAIK MASTHAN BASHA',
                 '20KB1A03A4': 'SHAIK MOHAMMAD', '20KB1A03A5': 'SHAIK THOHID', '20KB1A03A6': 'SHAIK VALIVULLA',
                 '20KB1A03A7': 'SIMBOTHU GANESH', '20KB1A03A8': 'SINGAMALA GURAVAIAH', '20KB1A03A9': 'SYED AYUB',
                 '20KB1A03B0': 'SYED MOHAMMED SAAD', '20KB1A03B1': 'TEEPALAPUDI SAISARATH',
                 '20KB1A03B2': 'THUMMURU VENKATESWARLU', '20KB1A03B3': 'TUNGA VISHNUVARDHAN REDDY',
                 '20KB1A03B4': 'UDATHA MAHESH', '20KB1A03B5': 'UMESH CHANDRA PANCHETI',
                 '20KB1A03B6': 'UPPUTURI YASWANTH', '20KB1A03B7': 'VAJRALA VISHNU', '20KB1A03B8': 'VALLURU GURU SAI',
                 '20KB1A03B9': 'VALLURU LIKITH', '20KB1A03C0': 'VANIPENTA KODANDARAMI REDDY',
                 '20KB1A03C1': 'VANKAYALA VASU', '20KB1A03C2': 'VANTHERAPALLI JAMES AGAPE',
                 '20KB1A03C3': 'VELUGU GURUVENKATA SAIJITHIN', '20KB1A03C4': 'VELUGU VARUN TEJA',
                 '20KB1A03C5': 'VENATI MAHESH', '20KB1A03C6': 'VENDOTI VISHNU', '20KB1A03C7': 'YEDDU RAHUL',
                 '20KB1A03C8': 'YERRABOTHU SAMYOOL', '20KB1A0565': 'KONDURU DAKSHAYANI ',
                 '20KB1A0566': 'KONDURU MANOGNA ', '20KB1A0567': 'KONDURU PRANEETHA ',
                 '20KB1A0568': 'KOTA PRATHYUSHA ', '20KB1A0569': 'KUKATI GOWTHAM', '20KB1A0570': 'KUNCHAPU RAJESH',
                 '20KB1A0571': 'KUNDERU SREERAJ KRISHNA', '20KB1A0572': 'KURMA MEGHANA ',
                 '20KB1A0573': 'KUSETTY VAMSIKRISHNA', '20KB1A0574': 'LINGUTLA RAVINDRA',
                 '20KB1A0576': 'MADIRA SIDDA SAI VARAPRASAD', '20KB1A0577': 'MALCHI SINDHUJA ',
                 '20KB1A0578': 'MALLAVARAM JAHNAVI ', '20KB1A0579': 'MALLE PRANAV DHEERAJ',
                 '20KB1A0580': 'MANNEPALLI MOUNIKA ', '20KB1A0581': 'MANNURU MAHIDHAR',
                 '20KB1A0582': 'MARAKALAKUPPAM PRAMOD KUMAR', '20KB1A0583': 'MARRI MAHESH',
                 '20KB1A0584': 'MARRI SAI SUDHEEPA ', '20KB1A0585': 'MEKALA VAMSI', '20KB1A0586': 'MIDATHA PALLAVI ',
                 '20KB1A0587': 'MOGILI HEMANTH', '20KB1A0588': 'MOHAMMED GULSHAN ',
                 '20KB1A0589': 'MOHAMMED JAKEER HUSSAIN', '20KB1A0590': 'MORAVANENI SAI KRISHNA',
                 '20KB1A0591': 'MUCHU VENKATA NARESH', '20KB1A0592': 'MUNGARA NAGA SAI CHETHAN',
                 '20KB1A0593': 'MUPPALA SUSHMA ', '20KB1A0594': 'MURTHAPPAGARI BHAVANIPRASAD',
                 '20KB1A0595': 'NANDIGAM BOBBY', '20KB1A0596': 'NANDURI HEMANTH LAKSHMI NARASARAJU',
                 '20KB1A0597': 'NATAKARANI MOHANSAI', '20KB1A0599': 'NEELURU AKHILA ',
                 '20KB1A05A0': 'NELLORE DAIZY MANASWITHA ', '20KB1A05A1': 'NELLORE PAVANI ',
                 '20KB1A05A2': 'NILAM PRUDHVI', '20KB1A05A3': 'NIMMAKAYALA CHARAN KUMAR',
                 '20KB1A05A4': 'OJILI BHAVANA ', '20KB1A05A5': 'OSURU DIVYA ',
                 '20KB1A05A6': 'PAGADALA MUNI PRANEETH REDDY', '20KB1A05A7': 'PALEPU MANEESHA ',
                 '20KB1A05A8': 'PAMANJI PALLAVI ', '20KB1A05A9': 'PANDALA BHOOMIKA SARVANI ',
                 '20KB1A05B0': 'PANDI PRAVEEN', '20KB1A05B1': 'PANDI SAI TEJA', '20KB1A05B2': 'PANTA VAISHNAVI ',
                 '20KB1A05B3': 'PASALA GANESH', '20KB1A05B4': 'PASALA LAHARI ',
                 '20KB1A05B5': 'PENUDOTA VENKATA VARAPRASAD', '20KB1A05B6': 'PETA DHANUSH',
                 '20KB1A05B7': 'PILLARISETTY JOSHMITHA ', '20KB1A05B8': 'PITCHIKA MUNI PRAVEEN',
                 '20KB1A05B9': 'POLURU GREESHMA ', '20KB1A05C0': 'POOLA MUNI VENKATA AJAY KUMAR',
                 '20KB1A05C1': 'PORUMAMILLA KAVYA ', '20KB1A05C2': 'POTTIPATI ARUN KUMAR REDDY',
                 '20KB1A05C3': 'PRATHIBHA PUVVADA ', '20KB1A05C4': 'PRUDHVI KRISHNA TEJA',
                 '20KB1A05C5': 'PRUDHVI VINAY KUMAR', '20KB1A05C6': 'PUCHALAPALLI ANIL',
                 '20KB1A05C7': 'PUCHALAPALLI YOSHITHA ', '20KB1A05C8': 'PUDI RENU BHARGAVI ',
                 '20KB1A05C9': 'PULIKONDA SAI SUNANDA ', '21KB5A0507': 'PACCHIPALA VENKATA UMESH',
                 '21KB5A0508': 'KOMMI LAKSHMI SOWJANYA ', '21KB5A0509': 'POKURU THANUJA ',
                 '21KB5A0510': 'NAGALA SAITEJA', '21KB5A0511': 'KARUPARTHY JYOTHI SAI RAJU',
                 '21KB5A0512': 'JAYAPRAKASH SATYA PRAKASH', '20KB1A0465': 'KARAMVALLI CHALL MUKHADDAS ',
                 '20KB1A0466': 'KARIKETI REMA HELAN ', '20KB1A0467': 'KARIPAKA PAVAN SAI',
                 '20KB1A0468': 'KATHA NIHITHA ', '20KB1A0469': 'KATTA SAI TEJA', '20KB1A0470': 'KEERTHIPATI DEEPTHIKA ',
                 '20KB1A0471': 'KETHINENI JAYA KRISHNA', '20KB1A0472': 'KOKOLLU VAISHNAVI ',
                 '20KB1A0473': 'KOLE PRAMODH', '20KB1A0474': 'KOMATIGUNTA VENKAT NIVAS',
                 '20KB1A0475': 'KOMMI JAYASANKAR', '20KB1A0476': 'KONDURU RAKESH', '20KB1A0477': 'KONIDENA SWATHI ',
                 '20KB1A0478': 'KOTA JAGANMOHAN REDDY', '20KB1A0479': 'KOVURU JYOTHIKA ',
                 '20KB1A0480': 'KUMMARI GURU MOHAN', '20KB1A0481': 'KUNDURTHI SARATHCHANDU',
                 '20KB1A0482': 'KUNKU VENKATA SREEJA ', '20KB1A0483': 'LAKKU SRI LAKSHMI ',
                 '20KB1A0484': 'MADHU CHANDU', '20KB1A0485': 'MADIRI VENKATA SAI', '20KB1A0486': 'MAJJI SRIKANTH',
                 '20KB1A0487': 'MALEPATI VISHNUVARDHAN REDDY', '20KB1A0488': 'MALLADI GURU CHARAN',
                 '20KB1A0489': 'MALLE CHAITHANYA ', '20KB1A0490': 'MALLI BINDHU MADHAVI ',
                 '20KB1A0491': 'MANAMALA ANVITHA ', '20KB1A0492': 'MANDA POOJITHA ',
                 '20KB1A0493': 'MANGALAGIRI NAGUR VALI', '20KB1A0494': 'MANGALI SUMANTH',
                 '20KB1A0495': 'MANNURU JAVEDAKBAR', '20KB1A0496': 'MARELLA JASWANTH',
                 '20KB1A0497': 'MARRI GEETHIKA SRAVYA ', '20KB1A0498': 'MARTHALA MANJULA ',
                 '20KB1A04A0': 'MAVUDURU NISHITHA ', '20KB1A04A1': 'MAVUDURU SONIYA ',
                 '20KB1A04A2': 'MEDANOOLU VEDITHA ', '20KB1A04A3': 'MOCHARLA LAKSHMIPRIYA ',
                 '20KB1A04A4': 'MOHAMMED NOORUL HASSAIN', '20KB1A04A5': 'MUDURU GOWHITH',
                 '20KB1A04A6': 'MULE MADHUSUDHAN REDDY', '20KB1A04A7': 'MUMMADI SUJITHA ',
                 '20KB1A04A8': 'MUTHUKURU RAJASEKHAR', '20KB1A04A9': 'NADENDLA SAAJIDH SAHEB',
                 '20KB1A04B0': 'NARAPAREDDY SAI KOWSHIK REDDY', '20KB1A04B1': 'NARAYANA PRATHEESH KUMAR',
                 '20KB1A04B2': 'NARE UDAY KUMAR REDDY', '20KB1A04B3': 'NATAKARANI SIVAIAH',
                 '20KB1A04B4': 'NAVIDI YAGNITHA ', '20KB1A04B5': 'NELANAKULA NAVYA ',
                 '20KB1A04B6': 'NIDIGUNTA PRAVEENA ', '20KB1A04B7': 'NUTHALAPATI GANESH',
                 '20KB1A04B8': 'NUTHI PENCHALA VISWAS', '20KB1A04B9': 'OVERS JOHNNY',
                 '20KB1A04C0': 'PACCHARIMEKALA MADHU', '20KB1A04C1': 'PAIDIMANI SARATH CHANDRA',
                 '20KB1A04C2': 'PAMUJULA SUDEEPTHI ', '20KB1A04C3': 'PANDI VENKATA SAI',
                 '20KB1A04C4': 'PANDILLAPALLI MONISHA ', '20KB1A04C5': 'PANTRANGAM MUNI RAKESH',
                 '20KB1A04C6': 'PATCHA PAVAN KUMAR', '20KB1A04C7': 'PATNAM NANDU ', '20KB1A04C8': 'PATTUKOTA ANUSHA ',
                 '21KB5A0407': 'VALLEPU ANUSHA ', '21KB5A0408': 'YANAMALA MANASA ',
                 '21KB5A0409': 'MODUGAPALYAM MEGHANADHAM REDDY', '21KB5A0410': 'DASARI PAVAN GANESH',
                 '21KB5A0411': 'GUNJI SRINIVASA TEJA', '21KB5A0412': 'CHAPRAM PRAMEELA ',
                 '20KB1A0246': 'MUDDULURU YASWANTH RAJU', '20KB1A0247': 'NALAGALA SUMASREE ',
                 '20KB1A0248': 'NALAGARLA SRILATHA ', '20KB1A0249': 'NANDA PRAGNA ', '20KB1A0250': 'PALA GOVARDHAN',
                 '20KB1A0251': 'PALLIMETI VAMSI', '20KB1A0252': 'PASUPULETI SONIYA ', '20KB1A0253': 'PITTI ANUSHA ',
                 '20KB1A0254': 'POLURU NESTHA ', '20KB1A0255': 'PULAKANTI RAJESH', '20KB1A0256': 'PUTCHALAPALLI AJAY',
                 '20KB1A0257': 'RAYAPU VARSHITH', '20KB1A0258': 'SAMADHI DIVYA ', '20KB1A0259': 'SAMADHI VINAY KUMAR',
                 '20KB1A0260': 'SANNIBOINA VENKATA SIVA', '20KB1A0261': 'SHAIK ALTHAF', '20KB1A0262': 'SHAIK ARSHAD',
                 '20KB1A0263': 'SHAIK RUHIN ', '20KB1A0264': 'SHAIK SHARMILA ', '20KB1A0265': 'SHAKHAPURAM SRIHARI',
                 '20KB1A0266': 'SRIKIREDDY HARSHITHA ', '20KB1A0267': 'SUNKIREDDY PRAVEEN KUMAR',
                 '20KB1A0268': 'SYED MOHAMMAD RAFI', '20KB1A0269': 'THAMBI DIGNESH', '20KB1A0270': 'THAMMI MADHAN',
                 '20KB1A0271': 'THANDRA SAI KRISHNA', '20KB1A0272': 'THEPALAPUDI SATHYA ',
                 '20KB1A0273': 'THIRUPATHI NAVEEN KUMAR', '20KB1A0274': 'THOTA KRISHNA TEJA',
                 '20KB1A0275': 'UDAYAGIRI HIMA BINDHU ', '20KB1A0276': 'UPPALA SANDHYA ',
                 '20KB1A0277': 'VADLAPUDI MANJUNADHAM', '20KB1A0278': 'VADLAPUDI MANOREETHIKA ',
                 '20KB1A0279': 'VARIGONDA VENKATA VYSHNAVI KUMARI ', '20KB1A0280': 'VATAMBEDU NIHARIKA ',
                 '20KB1A0281': 'VATTIKAYALA SINDHU ', '20KB1A0282': 'VAVILI CHANDUPRIYA ',
                 '20KB1A0283': 'VEERABOINA REVANTH', '20KB1A0284': 'VEERAMREDDY SAI TEJA REDDY',
                 '20KB1A0285': 'VELURU HEMA NANDITHA ', '20KB1A0286': 'VENNAPUSA MAHITHA ',
                 '20KB1A0287': 'VETA HARI BABU', '20KB1A0288': 'YANAMALA CHANDRASANJAY',
                 '20KB1A0289': 'YARRATI JITHENDRA', '20KB1A0290': 'YASARLA SAI KIRAN',
                 '19KB1A0244': 'NAGISETTY AJAY KUMAR', '21KB5A0212': 'JADAPALLI SAI KRISHNA',
                 '21KB5A0213': 'ARUMULLA YASWANTH', '21KB5A0214': 'TUPAKULA UDAY KUMAR',
                 '21KB5A0215': 'MUPPALA BHARADWAJ', '21KB5A0216': 'ERAGARAJU CHINNI KRISHNA',
                 '21KB5A0217': 'BODDU SAI KRISHNA', '21KB5A0218': 'DONIPARTHI SARVAN KUMAR',
                 '21KB5A0219': 'YANAMALA NARENDRA KUMAR', '21KB5A0220': 'DESIREDDY RAJESHREDDY',
                 '21KB5A0221': 'INGILALA MARY VATHSALYA ', '21KB5A0222': 'DASARI BHAVADEEP',
                 '20KB1A0141': 'MUNAMALA RAKESH', '20KB1A0142': 'NASAM LOKESH', '20KB1A0143': 'NAVURU GUNEENDRA',
                 '20KB1A0144': 'OREPALLI AJAY', '20KB1A0145': 'PALAPARTHI GEERTHIKA ', '20KB1A0146': 'PAMUJULA SUKESH',
                 '20KB1A0147': 'PASUPULETI DURGAPRASAD', '20KB1A0148': 'PATAN FAIZAN', '20KB1A0149': 'PAVALLA MAHENDRA',
                 '20KB1A0150': 'PEDDIREDDY RAGHU CHETHAN', '20KB1A0151': 'PENDYALA KAVYA ',
                 '20KB1A0152': 'PERAM KAVYA ', '20KB1A0153': 'PERUBOYINA SATHISH', '20KB1A0154': 'RAVI DILEEP KUMAR',
                 '20KB1A0155': 'RAVILLA BALU GUNASEKHAR', '20KB1A0156': 'SEERLA SIVA SAI',
                 '20KB1A0157': 'SHAIK AADIL AHAMED', '20KB1A0158': 'SHAIK ASIF', '20KB1A0159': 'SHAIK SAJJAD HUSSAIN',
                 '20KB1A0160': 'SHAIK SAMIYA ', '20KB1A0161': 'SHAIK SIDDIQ', '20KB1A0162': 'SRIRAM JAI HANUMA',
                 '20KB1A0163': 'THANGAM ARUNACHALAM', '20KB1A0164': 'THEEPALAPUDI LOKESH',
                 '20KB1A0165': 'THIRUMURU YASWANTH', '20KB1A0166': 'TUTIVAKA BHARGAV REDDY',
                 '20KB1A0167': 'UDATHA DEEPAKTEJA', '20KB1A0168': 'VAGGALA SADHANA ',
                 '20KB1A0169': 'VARIKUNTLA PAVANSAI', '20KB1A0170': 'VATAMBETI MURUGESH',
                 '20KB1A0171': 'VEDULA DEEDEEPYA ADARSH', '20KB1A0172': 'VELPULA MAHENDRA REDDY',
                 '20KB1A0173': 'VEMA MUNI ESWARA RAGHAVA', '20KB1A0174': 'VETA SUPRIYA ',
                 '20KB1A0175': 'YAMPALLA BADRI', '20KB1A0176': 'YARRAGUDI ABHILASH REDDY',
                 '20KB1A0177': 'YENDETI VIVEK', '20KB1A0178': 'YENUGU DWARAKANATHA REDDY',
                 '20KB1A0179': 'PERUMALLA MEGHANA ', '21KB5A0115': 'ARUMULLA VENKATA NARASIMHA',
                 '21KB5A0116': 'KRISHNAPATNAM KUSHAL KUMAR', '21KB5A0117': 'THULLURU MANISH KUMAR',
                 '21KB5A0118': 'GONUGUNTA VENKATA PRAVEEN', '21KB5A0119': 'PERIKALA BHARGAV',
                 '21KB5A0120': 'KATHI DURGESH', '21KB5A0121': 'SHAIK USMAN', '21KB5A0122': 'KORRAPATI GREESHMA ',
                 '21KB5A0123': 'BOMMAJI SUNDARA RAO', '21KB5A0124': 'CHILAKAPATI MAHESH',
                 '21KB5A0125': 'PAGIPATI NAGABALA', '21KB5A0126': 'NAVURU KOTESWARA RAO',
                 '21KB5A0127': 'PATI CHANDRAKANTH', '21KB5A0128': 'GRANDHIVEMULA KISHAN KUMAR REDDY',
                 '21KB5A0129': 'MUDDISETTY DAYANANDA SARASWATHI', '21KB5A0130': 'GANGAVARAM GANGI REDDY',
                 '21KB5A0301': 'INGILALA ANVESH', '21KB5A0302': 'SANAGA SANATH KUMAR',
                 '21KB5A0303': 'MANGALAPURI SAI KIRAN', '21KB5A0304': 'EEDURU DHARMENDRA',
                 '21KB5A0305': 'PONNAGANTI BHUVANA CHANDRA', '21KB5A0306': 'PAYANAM UDAY SATWIK',
                 '21KB5A0307': 'SHAIK MANSOOR', '21KB5A0308': 'ANEPUDI HARISH', '21KB5A0309': 'GADELA SAMAVEDA',
                 '21KB5A0310': 'SHAIK MOHAMMED THOUSIF', '21KB5A0311': 'ULSA VAMSIKRISHNA',
                 '21KB5A0312': 'VENGALLATHURU MOKSHAGNA', '21KB5A0313': 'NALAGONDLA SANDEEP',
                 '21KB5A0314': 'SIDDAVARAM SAI KALYAN', '21KB5A0315': 'SHAIK AHMED RAKHIL',
                 '21KB5A0316': 'LAKKU VARSHA VARDHANA KUMAR', '21KB5A0317': 'SHAIK AZAR',
                 '21KB5A0318': 'MEKALA DIVAKAR', '21KB5A0319': 'KAVETI VIJAY KUMAR',
                 '21KB5A0320': 'SK MD NASIF HASSAIN', '21KB5A0321': 'SATHYAVETI VENKATNAVEEN KUMAR',
                 '21KB5A0322': 'SHAIK MUZAMEL SALEEM', '21KB5A0323': 'SHAIK JAMEEL AHMAD',
                 '21KB5A0324': 'POORIMITLA YASWANTH', '21KB5A0325': 'GANGABATHINA SAMPATH KUMAR',
                 '21KB5A0326': 'SADHU KISHORE', '21KB5A0327': 'BODIKALA SANTHOSH', '21KB5A0328': 'DATTAM GURUPRASAD',
                 '21KB5A0329': 'RAGIPATI PRADEEP', '21KB5A0330': 'SEELAMSETTY TEJA', '21KB5A0331': 'GUTHA UDAY KUMAR',
                 '21KB5A0332': 'ODURU VINAY KUMAR', '21KB5A0333': 'MOHAMMAD FARHAN AHAMAD',
                 '21KB5A0334': 'SHAIK SULTHAN BASHA', '21KB5A0335': 'SYED ASHRAF', '21KB5A0336': 'SHAIK JANNATH HUSSEN',
                 '21KB5A0337': 'KATA CHANDRAMUNI SWAMY', '21KB5A0338': 'PEDDAMALLU BHARATH KUMAR REDDY',
                 '21KB5A0339': 'RAVILLA DINESH', '21KB5A0346': 'THULAKANAM JASWANTH',
                 '21KB5A0347': 'KANDALA BHANU PRAKASH YADAV', '21KB5A0348': 'SHAIK ARSHAD', '21KB5A0349': 'Unknown',
                 '21KB5A0340': 'CHINTHA MUNI KIRAN', '21KB5A0341': 'KUCHI SATHISH', '21KB5A0342': 'NASINA KARTHIK',
                 '21KB5A0343': 'DAMAVARAPU PAVAN', '21KB5A0344': 'SHAIK LATHEEF',
                 '21KB5A0345': 'VALLEPU PRADEEP CHANDU', '20KB1A05D0': 'PUNAMALLI SUNEEL',
                 '20KB1A05D1': 'PUNDLA EESHITHA ', '20KB1A05D2': 'PUTTAM ANKAIAH', '20KB1A05D3': 'RAGIPATI SAI KISHORE',
                 '20KB1A05D4': 'RAMABATHINA LAKSHMI PRIYA ', '20KB1A05D5': 'RAPURU ARAVIND KUMAR',
                 '20KB1A05D6': 'RAVULA SRINIVAS', '20KB1A05D7': 'REDDIPALLI THEJESHKUMAR',
                 '20KB1A05D8': 'RUDRARAJU PRUDVI RAJU', '20KB1A05D9': 'S V S S KOUSHIK SIDDHARDHA',
                 '20KB1A05E0': 'SAJJA PUSHPASREE ', '20KB1A05E1': 'SAJJA SRIKANTH', '20KB1A05E2': 'SAMPATHI MANOJ',
                 '20KB1A05E3': 'SAMUDRALA EESHITHA ', '20KB1A05E4': 'SANA RANJITH',
                 '20KB1A05E5': 'SANNAPPA VISHNU VARDHAN', '20KB1A05E6': 'SANNAREDDY KASTHURI REDDY',
                 '20KB1A05E7': 'SARIPARALLA ANUSHA ', '20KB1A05E8': 'SATHENAPALLI ANITHA ',
                 '20KB1A05E9': 'SETTIPALLI NANDA MOHAN REDDY', '20KB1A05F0': 'SHAIK KARIMULLA',
                 '20KB1A05F1': 'SHAIK KARISHMA ', '20KB1A05F2': 'SHAIK LATHEEF', '20KB1A05F3': 'SHAIK MUJEEB',
                 '20KB1A05F4': 'SHAIK RAMEEZ', '20KB1A05F5': 'SHAIK SADIK', '20KB1A05F6': 'SHAIK THASLEEM ',
                 '20KB1A05F7': 'SIDDAM HARIKA ', '20KB1A05F8': 'SRIPATHI REDDY HARSHA VARDHAN',
                 '20KB1A05F9': 'SYED MOHAMMAD ALI', '20KB1A05G0': 'TADIPATRI LAVANYA ', '20KB1A05G1': 'TALLA BHARATHI ',
                 '20KB1A05G2': 'THALLAPALLI RUCHITHA ', '20KB1A05G3': 'THALLURU BABITHA CHOWDARY ',
                 '20KB1A05G4': 'THATIGALLA VENKATA RAMANA', '20KB1A05G5': 'THATIPARTHI HARSHAVARDHAN REDDY',
                 '20KB1A05G6': 'THOGUNTA PRATHYUSHA ', '20KB1A05G7': 'THONNATI VENKATA GURU TEJA',
                 '20KB1A05G8': 'THUMMALA LAKSHMI ANKITHA ', '20KB1A05G9': 'THUMMUKURU NIKHILESH',
                 '20KB1A05H0': 'THUPILI GURU PRAKASH', '20KB1A05H1': 'TIRUMALASETTY HARIKA ',
                 '20KB1A05H2': 'TOLUSURI PRATHYUSHA ', '20KB1A05H3': 'TUNIKALA MUNESH BABI',
                 '20KB1A05H4': 'TUPILI SREENATH', '20KB1A05H5': 'UPPUGUNDURI BHARADWAJ', '20KB1A05H6': 'V VARNITHKUMAR',
                 '20KB1A05H7': 'VADLAPALLI SIREESHA ', '20KB1A05H8': 'VAKATI SRAVANI ',
                 '20KB1A05H9': 'VANJAVAKA SUDEEP KUMAR', '20KB1A05I0': 'VARTHA VARSHITH',
                 '20KB1A05I1': 'VELLAMPALLI LAKSHMI PRIYA ', '20KB1A05I2': 'YADAVALLI AJITHA ',
                 '20KB1A05I3': 'YAKASIRI TEJASWINI ', '20KB1A05I4': 'YALAMANDALA FATIMABI ',
                 '20KB1A05I5': 'YALLAMGARI VINEETH', '20KB1A05I6': 'YALLAMPATI HIMABINDU ',
                 '20KB1A05I7': 'YANAMADALA MANOJ KUMAR', '20KB1A05I8': 'YANNABATHINA BALAJI',
                 '20KB1A05I9': 'YARAGARLA SUSMITHA ', '20KB1A05J0': 'YEDDALA VARSHA VANDANA ',
                 '20KB1A05J1': 'YEGATELA JITHENDRA', '20KB1A05J2': 'YERRAM LAKSHMI DEEPAK',
                 '20KB1A05J3': 'DAVA SRIVALLI ', '18KB1A05E0': 'SIDDAVATAM SIVAJI', '21KB5A0513': 'PIDATHALA RANJITHA ',
                 '21KB5A0514': 'SHAIK MUZAHIR', '21KB5A0515': 'ANJAMETI RAMESWAR',
                 '21KB5A0516': 'YAMPALLA BHARATH KUMAR', '21KB5A0517': 'DHODDAGA VIKKY',
                 '21KB5A0518': 'KALLUTLA BHANU PRAKASH', '20KB1A04C9': 'PEDDIREDDY SARATHCHANDRA REDDY',
                 '20KB1A04D0': 'PELLETI INDRASENA REDDY', '20KB1A04D1': 'PERAMBEDU MEGHANA ',
                 '20KB1A04D2': 'PETA DIVYA SAI ', '20KB1A04D3': 'PINJALA SUSHMA ', '20KB1A04D4': 'PONTHALA JISHITHA ',
                 '20KB1A04D5': 'POOLAMBETI LIKITH', '20KB1A04D6': 'POTLURU BHUVANESWARI ',
                 '20KB1A04D7': 'POTTEPALEM CHETHAN', '20KB1A04D8': 'PUDI JAHNAVI ',
                 '20KB1A04D9': 'PUDIPARTHI VENKATA SAI TEJA', '20KB1A04E0': 'PULLURU REKHA',
                 '20KB1A04E1': 'PURINI CHANDANA ', '20KB1A04E2': 'RACHAGOLLA HARI KRISHNA',
                 '20KB1A04E3': 'RAJA SRIRAM', '20KB1A04E4': 'RAMAKURU VENKATA RANGANATHA ABHIRAM',
                 '20KB1A04E5': 'RAVURU DILEEP', '20KB1A04E6': 'RUPIREDDY ESWAR', '20KB1A04E7': 'SATHI JEEVAN MADHUKAR',
                 '20KB1A04E8': 'SATYAVETI LALINYA ', '20KB1A04E9': 'SHAIK ANNU', '20KB1A04F0': 'SHAIK AYAZ AHAMED',
                 '20KB1A04F1': 'SHAIK FARHAN', '20KB1A04F2': 'SHAIK HUMERA ', '20KB1A04F3': 'SHAIK JASMIN ',
                 '20KB1A04F4': 'SHAIK MASTHAN BABU', '20KB1A04F5': 'SHAIK NAMAJI', '20KB1A04F6': 'SHAIK NAWAZ',
                 '20KB1A04F7': 'SHAIK NOWSHAD ', '20KB1A04F8': 'SHAIK PARVAZ', '20KB1A04F9': 'SHAIK RESHMA ',
                 '20KB1A04G0': 'SHAIK VASEEM', '20KB1A04G1': 'SHEIK SHAREEFUDDIN', '20KB1A04G2': 'SYDAM GOVINDA RAJU',
                 '20KB1A04G3': 'TALAPALA HARSHA SAI', '20KB1A04G4': 'TALATHOTI HANOK HERALD',
                 '20KB1A04G5': 'TALLURU SUKUMAR', '20KB1A04G6': 'THEEPALA PUDI LAVANYA ',
                 '20KB1A04G7': 'THERU PUJITHA ', '20KB1A04G8': 'THIKKA PRATHYUSHA ',
                 '20KB1A04G9': 'THIRAVATURU PAVANI ', '20KB1A04H0': 'THOOMATI PRANEETH REDDY',
                 '20KB1A04H1': 'TOLIKONDA SRAVANI ', '20KB1A04H2': 'TURAKA AJAY',
                 '20KB1A04H3': 'UKOTI VENKATA CHAITANYA', '20KB1A04H4': 'UNDELA PRASANNA ',
                 '20KB1A04H5': 'UPPALA RADHA ', '20KB1A04H6': 'VALASA VANDANA ', '20KB1A04H7': 'VEDAGIRI VAISHNAVI ',
                 '20KB1A04H8': 'VEERASWAMY BHAVANESH', '20KB1A04H9': 'VELURU HARSHA VARDHAN',
                 '20KB1A04I0': 'VELURU SAI KARTHIKEYA', '20KB1A04I1': 'VEMPALLA PAVANA CHANDRIKA ',
                 '20KB1A04I2': 'VEMPALLI MUNI GANESH', '20KB1A04I3': 'VEMPALLI POOJITHA ',
                 '20KB1A04I4': 'YADDALA HARI PRASAD REDDY', '20KB1A04I5': 'YAKKANTI GOVARDHAN REDDY',
                 '20KB1A04I6': 'YARRATI KARTHIK', '20KB1A04I7': 'YEDDULA PAVAN KUMAR REDDY ',
                 '20KB1A04I8': 'YEKULA SIDDARDHA', '20KB1A04I9': 'YELURU HARIPRIYA ', '20KB1A04J0': 'YENDOTI HEMANTH',
                 '20KB1A04J1': 'YERRAMUTHI PUSHPALATHA ', '21KB5A0413': 'KURUCHETI SOWMYA ',
                 '21KB5A0414': 'SHAIK SOFIA ', '21KB5A0415': 'BITRAGUNTA MANEESHA ', '21KB5A0416': 'KANTLAM SNIGDHA ',
                 '21KB5A0417': 'PENDLIKATLA VINAY KUMAR', '21KB5A0418': 'PATTI SAI RAHUL',
                 '21KB5A0419': 'MUKKAMALLA AKHIL KUMAR REDDY', '19KB1A1201': 'AMULURU DIVITHA ',
                 '19KB1A1202': 'ARAVA SMARAN', '19KB1A1203': 'CHEVURI VENKATA SAI RAMA GURUMURTHY',
                 '19KB1A1204': 'CHEVURU CHAITANYA', '19KB1A1205': 'CHITTA THARUN KUMAR REDDY',
                 '19KB1A1206': 'DODLA SAHITHI ', '19KB1A1208': 'G M YESHWANTH ESWAR', '19KB1A1209': 'GAJJELA REDDAIAH',
                 '19KB1A1210': 'GUDUR AJAY KUMAR REDDY', '19KB1A1211': 'HASTHI PRUDHVI',
                 '19KB1A1212': 'JAKKAM KISHORE REDDY', '19KB1A1213': 'KADIYALA SRAVANI ',
                 '19KB1A1214': 'KALIVILI SAI GAYATHRI ', '19KB1A1215': 'KANDLAKUTI AKHILA ',
                 '19KB1A1216': 'KANISETTY VENKATA SURENDRA TARUN GUPTHA', '19KB1A1218': 'KONANKI VENKATA SIVA SAITEJA',
                 '19KB1A1219': 'KONDURU YAMINI PRIYA ', '19KB1A1220': 'KORIVI VENKATA KEERTHI ',
                 '19KB1A1221': 'KORRAPATI SAI KIRAN NAIDU', '19KB1A1222': 'KOTA ARUN',
                 '19KB1A1223': 'KUNDERU DHEERAJ KRISHNA', '19KB1A1224': 'LEKKALA DINESH',
                 '19KB1A1225': 'MALAPATI PRIYA DARSHINI ', '19KB1A1226': 'MANIYAR KHAJA MOHINUDDIN',
                 '19KB1A1227': 'MURAMREDDY VANDANA ', '19KB1A1228': 'NAGINENI TEJASWANI ',
                 '19KB1A1229': 'NALLA VISHNU TEJA REDDY', '19KB1A1230': 'NARALA RAM PRAKASH REDDY',
                 '19KB1A1231': 'NELAVALA MADESH', '19KB1A1232': 'PANDILLAPALLI BALARAM REDDY',
                 '19KB1A1233': 'PAPAREDDY SAKETH', '19KB1A1234': 'PIDURU SRI DHANA ',
                 '19KB1A1235': 'POLAMREDDY ABHIGNA ', '19KB1A1236': 'PUTTAMREDDY SAICHAKRADHAR REDDY',
                 '19KB1A1237': 'RANGINENI RUPASRI ', '19KB1A1239': 'SAMUDRALA JEEVANA LAKSHMI ',
                 '19KB1A1240': 'SHAIK ABDUL KHALIQ', '19KB1A1241': 'SHAIK JASMINE FATHIMA ',
                 '19KB1A1242': 'SHAIK MOHIDDIN', '19KB1A1243': 'SHAIK SAFRIN ', '19KB1A1244': 'SHAIK SAMEER',
                 '19KB1A1245': 'SIDDAPAREDDY SIVAKUMAR REDDY', '19KB1A1246': 'SOLLETI YAMINI ',
                 '19KB1A1247': 'SOMISETTY SRAVYA ', '19KB1A1248': 'SWARNA PRATHIMA ',
                 '19KB1A1250': 'THUMMALA YASWANTH REDDY', '19KB1A1251': 'VARIKUTI SINDHU ',
                 '19KB1A1252': 'VEMULA MUNEESWAR', '19KB1A1253': 'YARRABAPU GOUTHAM REDDY',
                 '19KB1A1254': 'YELURU KARTHIKEYA REDDY', '19KB1A1255': 'YENUGANTI NAVEEN', '19KB1A0301': 'AMASA RAJA',
                 '19KB1A0302': 'AMRUTHAM TEJA', '19KB1A0303': 'ANNAVARAM NARENDRA', '19KB1A0304': 'ARAVABHUMI NIKHIL',
                 '19KB1A0305': 'ATHIVARAM SASI KUMAR', '19KB1A0306': 'ATHMAKURU VISHNU',
                 '19KB1A0307': 'BALLI SHALEM SAHITHYA SUKUMAR', '19KB1A0308': 'BELLAMKONDA BALAJI',
                 '19KB1A0309': 'BERI HARITEJA', '19KB1A0310': 'BHUMIREDDY HARI KRISHNA REDDY',
                 '19KB1A0311': 'BOJJA KALYANKUMAR', '19KB1A0312': 'C SUNNY',
                 '19KB1A0313': 'CHALLA VENKATA JANAKI UMESH VARDHAN', '19KB1A0314': 'CHALLA YASWANTH KUMAR',
                 '19KB1A0315': 'CHERUKUMUDI SASIDHARA SRIVATCHASA', '19KB1A0316': 'CHIRIPIREDDY MANOJ',
                 '19KB1A0317': 'DARA RAM', '19KB1A0318': 'DASARI RAMA CHARAN', '19KB1A0319': 'DODLA TARUN KUMAR REDDY',
                 '19KB1A0320': 'DODLA VIGNESH LOHITH', '19KB1A0322': 'EDURU SAI KRISHNA',
                 '19KB1A0323': 'GALIBOYINA THIRUPATHI BABU', '19KB1A0324': 'GALLA SRI SAI CHARAN',
                 '19KB1A0325': 'GANDLA LOKESH', '19KB1A0326': 'GANGAVARAM MANOJ', '19KB1A0327': 'GIRI SUKUMAR',
                 '19KB1A0328': 'GODA AAKASH MALLIK', '19KB1A0329': 'GONUPALLI AVINASH',
                 '19KB1A0330': 'GORRIPATI SAI SANJAY', '19KB1A0331': 'GOTTAM DHARANESH',
                 '19KB1A0332': 'GUDURU VIJAY ANAND', '19KB1A0333': 'GUDURU VISHNU VARDHAN',
                 '19KB1A0334': 'GUNDALA DUSHYANTH', '19KB1A0335': 'GUNDEBOINA RAJASEKHAR',
                 '19KB1A0336': 'JALADANKI VENKATA RAVI TEJA', '19KB1A0337': 'KAKARLA RAJESH',
                 '19KB1A0338': 'KALAHASTHI HARIKRISHNA', '19KB1A0339': 'KANDALA ROHITH KUMAR',
                 '19KB1A0340': 'KAPPARA VENKATA SAI KOUNDINYA YASWANTH', '19KB1A0341': 'KASI MOHANSAIKUMAR',
                 '19KB1A0342': 'KASUKURTHI SREEKAR SIDHARTHA', '19KB1A0343': 'KATHI GOPALAKRISHNA',
                 '19KB1A0344': 'KATI BALAJI', '19KB1A0345': 'KATIKALA SIDDI VINAY',
                 '19KB1A0347': 'KATTINA PRANAY KUMAR', '19KB1A0348': 'KAVERIPAKAM YOGESH',
                 '19KB1A0349': 'KOLE RAJA SEKHAR', '19KB1A0350': 'KOTAM REDDY HEMANTH REDDY',
                 '19KB1A0351': 'KUKATI SUMANTH', '19KB1A0501': 'AADI KOMALIKA ',
                 '19KB1A0502': 'AADIMULAM JEETHENDRA KUMAR', '19KB1A0503': 'ABBARAJU VENKATA NAGA SAI JESWANTH',
                 '19KB1A0505': 'ALIVA DEEPALI OJHA ', '19KB1A0506': 'ALLAMPATI JANANI ',
                 '19KB1A0507': 'ALLI SARATH BABU', '19KB1A0508': 'ALLURU RAMU', '19KB1A0509': 'AMBATI ANUDEEP REDDY',
                 '19KB1A0510': 'ANAPALLI GURUPREETHAM REDDY', '19KB1A0511': 'ANDALAMALA KEERTHANA ',
                 '19KB1A0512': 'ANNAMETI ROSHITHA ', '19KB1A0513': 'ANNEM VENKATA SAI REVANTH KUMAR REDDY',
                 '19KB1A0514': 'ARCHAKAM MADHAVAGIRI SAI CHARITH', '19KB1A0515': 'ATIGADDA SUSMITHA ',
                 '19KB1A0516': 'ATLA RAJESWARI ', '19KB1A0517': 'ATLA THULASI ', '19KB1A0518': 'AVULA DHAN RAJ',
                 '19KB1A0519': 'BANDIKATLA LOKESH SAI', '19KB1A0520': 'BATCHU VENKATA SAI RISHITHA ',
                 '19KB1A0521': 'BATTA SUMANTH', '19KB1A0522': 'BHATTA VENKATA NAGA SAI TARUN',
                 '19KB1A0523': 'BODDU VENKATA TARUN', '19KB1A0524': 'BOLIGILA AKSHITHA ',
                 '19KB1A0525': 'BOLLINENI HEMANTH KUMAR', '19KB1A0526': 'CHAINRAJ CHETANA JAIN ',
                 '19KB1A0527': 'CHALLA DINESH', '19KB1A0528': 'CHALLA KEERTHI PRIYA ', '19KB1A0529': 'CHEJARLA CHITESH',
                 '19KB1A0530': 'CHELLA GANESH KALYAN', '19KB1A0531': 'CHERUKURU VENKATA SAI DIVYA ',
                 '19KB1A0532': 'CHIGURUPATI BHAVANA ', '19KB1A0533': 'CHILUKOTI DEVANANDH',
                 '19KB1A0534': 'CHINTHAKAYALA BALAJI', '19KB1A0535': 'CHINTHAPUDI AVINASH',
                 '19KB1A0536': 'CHINTHAPUDI KARTHIK', '19KB1A0537': 'CHOPPA RAGA SREYA ',
                 '19KB1A0538': 'DAGGUPATI CHAITHANYA', '19KB1A0539': 'DANDOLU RAJESWARI ',
                 '19KB1A0540': 'DASARI MAHESH', '19KB1A0541': 'DASARI VINOD KUMAR',
                 '19KB1A0542': 'DUMPALA PRABHU SUKETH', '19KB1A0543': 'EDIGA LALITHA ',
                 '19KB1A0544': 'EGALAPATI AKHIL KUMAR', '19KB1A0545': 'ELAPA ABHISHEK',
                 '19KB1A0546': 'ERAGAMREDDY LAKSHMI PRIYANKA ', '19KB1A0547': 'ESWARARAJU SAI VARMA',
                 '19KB1A0548': 'GAJJALA MANASA ', '19KB1A0549': 'GANGAVARAPU MANMOHAN REDDY',
                 '19KB1A0550': 'GONU VINEELA ', '19KB1A0551': 'GOSETTY MADHU', '19KB1A0552': 'GUBALA BHAVANA ',
                 '19KB1A0553': 'GUJJALAPUDI LAKSHMI PRIYA ', '19KB1A0554': 'GUNDALA SASI KUMAR',
                 '19KB1A0555': 'GUNDAPANENI POORVIKA CHOWDARY ', '19KB1A0556': 'GUNNAMREDDY SRIVARDHAN REDDY',
                 '19KB1A0557': 'GUNTAMADUGU GAYATHRI ', '19KB1A0558': 'GUNUKULA VENKATESH',
                 '19KB1A0559': 'JAKKAMREDDY SUDEEPA ', '19KB1A0560': 'JANGA VASAVI ', '19KB1A0561': 'KADAPA HARIPRIYA ',
                 '19KB1A0562': 'KAKI CHANDANA ', '19KB1A0563': 'KALLURU LALITHYA ', '19KB1A0564': 'KALTIREDDY YASWANTH',
                 '20KB5A0501': 'V. LOKESH', '20KB5A0502': 'G. YASWITHA ', '20KB5A0503': 'G. LAVANYA ',
                 '20KB5A0504': 'D. MANASA ', '20KB5A0505': 'V. DEVARAJULU', '20KB5A0506': 'D. JAGADEESH',
                 '16KB1A0553': 'GUNDUBOINA GIREESH', '19KB1A0401': 'AARANI GOPI', '19KB1A0402': 'ALLAM BHANUSATHVIKA ',
                 '19KB1A0403': 'AMBATI LOKESH', '19KB1A0404': 'AMBATI SARANYA ', '19KB1A0405': 'AMMINENI THEJASWANI ',
                 '19KB1A0406': 'ANUMAREDDY SANDEEP KUMAR REDDY', '19KB1A0407': 'ARAVA SWAPNA ',
                 '19KB1A0408': 'ATMAKUR VINOD KUMAR', '19KB1A0409': 'ATTIPATLA MUNIKUMAR',
                 '19KB1A0410': 'AVULA SRINADH', '19KB1A0411': 'BADDIPUDI SREECHARAN',
                 '19KB1A0412': 'BANALA DHANALAKSHMI ', '19KB1A0413': 'BANDI SIREESHA ',
                 '19KB1A0414': 'BATTREDDY YASWANTH', '19KB1A0415': 'BAYINENI THARUN KUMAR',
                 '19KB1A0416': 'BESTAVEMULA YUVATEJA', '19KB1A0417': 'BOJJA KEERTHANA ',
                 '19KB1A0418': 'BOLIGARLA CHARAN KUMAR', '19KB1A0419': 'BOLLINENI HARSHITHA ',
                 '19KB1A0420': 'BONIGI LIKHITH HASIN', '19KB1A0421': 'BUDAMAGUNTA INDU ',
                 '19KB1A0422': 'BUSIREDDY UDAY KUMAR REDDY', '19KB1A0423': 'CHAMARTHI JAYASREE ',
                 '19KB1A0424': 'CHEDARLA VINAY KUMAR', '19KB1A0425': 'CHEDURUPAKU VASUNDHARA ',
                 '19KB1A0426': 'CHEMBETI MADHURI ', '19KB1A0427': 'CHENJI ROHITHA ', '19KB1A0428': 'CHERUKU SIVANI ',
                 '19KB1A0429': 'CHERUKUMUDI RAMAKRISHNA', '19KB1A0430': 'CHERUKURI RAJU',
                 '19KB1A0431': 'CHEVURU THIMOTHY TILAK', '19KB1A0432': 'CHINTHALA RUPASRI ',
                 '19KB1A0433': 'CHITTETI LIKHITHA ', '19KB1A0434': 'CHOPPALA LEELAVAISHNAVI ',
                 '19KB1A0435': 'DAKAVARAM PANIDHAR', '19KB1A0436': 'DARIMADUGU NARAYANA NANDA NEERAJ',
                 '19KB1A0437': 'DASARI USHA ', '19KB1A0438': 'DHAMAVARAPU LOHITHA ', '19KB1A0439': 'E RAKSHANA ',
                 '19KB1A0440': 'EDHURU SINDHU ', '19KB1A0441': 'GALI MADHURI ', '19KB1A0442': 'GANAKALA LIKHITHA ',
                 '19KB1A0443': 'GANESHAM PRIYANKA ', '19KB1A0444': 'GANGAVARAM NEELIMA ',
                 '19KB1A0445': 'GANGIREDDY SANJEEV KUMAR REDDY', '19KB1A0446': 'GANTA JAYANTH',
                 '19KB1A0447': 'GARIKAPATI MAHARSHI', '19KB1A0448': 'GOLLAPUDI VENKATA SUNIL REDDY',
                 '19KB1A0449': 'GOTTAM DHANASEKHAR', '19KB1A0450': 'GUDURU MEGHANA ',
                 '19KB1A0451': 'GUNDALA HEMA CHANDANA ', '19KB1A0452': 'GUNDUBOINA HEMALATHA ',
                 '19KB1A0453': 'GUNDUBOYINA KAVYA ', '19KB1A0454': 'GUNTAGANI UJJEEV KUMAR',
                 '19KB1A0455': 'JARUGUMALLI VENKATA SAI TEJA', '19KB1A0456': 'JILAKARA VANDANA ',
                 '19KB1A0457': 'K S CHARAN RAJ', '19KB1A0458': 'KADIVETI YAMUNA ', '19KB1A0459': 'KAKUTURU MAHESH BABU',
                 '19KB1A0460': 'KALLAGUNTA AMRUTHA ', '19KB1A0461': 'KAMIREDDY HARSHITHA ',
                 '19KB1A0462': 'KANDALA SUMANTH', '19KB1A0463': 'KANDIKATLA KALYAN', '19KB1A0464': 'KANIMBAKAM MUNEESH',
                 '19KB1A0201': 'ALIMILI SIVA', '19KB1A0202': 'ALLADI RAJENDRA',
                 '19KB1A0203': 'AMBATI VENKATA VISWANADHA REDDY', '19KB1A0204': 'ANKU GURU SAI',
                 '19KB1A0205': 'ARANI POOJA ', '19KB1A0206': 'ARURU PRAVALLIKA ', '19KB1A0207': 'B. RAKESH NANDAN',
                 '19KB1A0208': 'BADI DINESH REDDY', '19KB1A0209': 'BADVELU CHANDANA ',
                 '19KB1A0210': 'BALAMPALLI VIJAYALAKSHMI ', '19KB1A0211': 'BOLLINENI SASIDHAR',
                 '19KB1A0212': 'CHEEKATI JAHNAVI ', '19KB1A0213': 'CHILLARA NAGA VENKATA SAI SRI AKHILA ',
                 '19KB1A0214': 'CHINTAMALLA SAI HEMANTH', '19KB1A0215': 'CHITTETI VAMSI',
                 '19KB1A0216': 'CHITTETI VARSHITH', '19KB1A0217': 'CHIYYARAPU VAMSI KRISHNA',
                 '19KB1A0218': 'DARLA BHUVANESWARI ', '19KB1A0219': 'DEVARAKONDA PURUSHOTHAM',
                 '19KB1A0220': 'DHAVALA SAI KUMAR', '19KB1A0221': 'DUVVURU VENKATESH BABU', '19KB1A0222': 'EGA VAMSI',
                 '19KB1A0223': 'GAJJALA VENKATA SASHIDHAR REDDY', '19KB1A0224': 'GEDA LEELA KRISHNA V S S N THEJASWI',
                 '19KB1A0225': 'GORTHALA VASU', '19KB1A0226': 'GUDDETI VASAVILATHA ',
                 '19KB1A0227': 'GUNISETTY PRAHELIKA ', '19KB1A0228': 'GURRAM PRAVALLIKA ',
                 '19KB1A0229': 'ITTAGUNTA NAGA SOWMYA ', '19KB1A0230': 'JAMALLA SREEJA ',
                 '19KB1A0231': 'JANGAM SREEJA ', '19KB1A0232': 'KADIMPATI SAI SUMANTH',
                 '19KB1A0233': 'KANDALA SATHYA VENKATA SAHITH KUMAR REDDY', '19KB1A0234': 'KARETI ANKAIAH',
                 '19KB1A0235': 'KASI REDDY VENKATA MANVITHA ', '19KB1A0236': 'KODIMUDI YASWANTH',
                 '19KB1A0237': 'KOMMI JAGAN', '19KB1A0238': 'KUMARAN POOJITHA ', '19KB1A0239': 'LAKKU SAI KEERTHI ',
                 '20KB5A0201': 'K. JASWANTH SAI', '20KB5A0202': 'A. SRINADH', '20KB5A0203': 'K. MANOJ KUMAR',
                 '20KB5A0204': 'M. POOJITHA ', '20KB5A0205': 'A. AKHILA ', '20KB5A0206': 'E. SRINADH',
                 '20KB5A0207': 'A. NARASIMHA', '20KB5A0208': 'V. JOHN HOSANNA', '20KB5A0209': 'P. THIRUMALESH',
                 '20KB5A0210': 'SHAIK. SAMEER AHAMED', '20KB5A0211': 'V. YUGA SUKRUTH', '20KB5A0212': 'G. BALA KRISHNA',
                 '20KB5A0213': 'G. ADILAKSHMI KAVYA ', '20KB5A0214': 'K. SUDHEER', '20KB5A0215': 'J. UDAY KUMAR',
                 '20KB5A0216': 'CH. VENKATESH', '20KB5A0217': 'M. ASHOK', '20KB5A0218': 'K. SANDEEP',
                 '20KB5A0219': 'A. PRANEETH', '20KB5A0220': 'N. SUPRASANTH', '20KB5A0221': 'C. LOKESH',
                 '19KB1A0101': 'ALLAMPATI AJITH', '19KB1A0103': 'BANKA SIVA', '19KB1A0104': 'BATTHALA SREEHARI',
                 '19KB1A0105': 'BILLA CHAKRADHAR', '19KB1A0106': 'BITRAGUNTA RUSHIDHAR REDDY',
                 '19KB1A0107': 'CHEEMAKURTHI GOKUL KRISHNA KUMAR', '19KB1A0108': 'CHEMBETI VENKATESH',
                 '19KB1A0109': 'CHIGERALA DELLI GANESH', '19KB1A0110': 'CHINTHAGUNTLA PRAVEEN KUMAR REDDY',
                 '19KB1A0111': 'DARA HARIKA ', '19KB1A0112': 'DEVARLA PRAVEEN',
                 '19KB1A0113': 'EDURU VENKATA SAI GANESH', '19KB1A0114': 'GOKARNAM MUNISANKAR',
                 '19KB1A0115': 'GUNDUBOYINA PAVAN KUMAR', '19KB1A0116': 'GUNDUBOYINA VENKATA SAI',
                 '19KB1A0117': 'KADEM LAKSHMAN', '19KB1A0118': 'KAKU THARUN KUMAR', '19KB1A0119': 'KALUVOY VENKAT RAJ',
                 '19KB1A0120': 'KANTABATHINA SRIRAM REDDY', '19KB1A0121': 'KAPULURU RUCHITHA REDDY ',
                 '19KB1A0122': 'KARANAM VINEETH', '19KB1A0123': 'KARLAPUDI VARMA', '19KB1A0124': 'KASARAM VINAY',
                 '19KB1A0125': 'KATAM HARIVARDHAN', '19KB1A0126': 'KAVALI THARUN KUMAR', '19KB1A0127': 'KAVETI AKASH',
                 '19KB1A0128': 'KONDAPURAM MANOJ SAI', '19KB1A0129': 'KORAKUTI DHAMODHAR', '19KB1A0130': 'KURUBA SHIVA',
                 '19KB1A0131': 'MALLI GOPI CHANDH', '19KB1A0132': 'MARTHALA SRINIVASULA REDDY',
                 '19KB1A0133': 'MEDA BADRI SRIVATSA', '19KB1A0134': 'MOOGA KISHORE',
                 '19KB1A0135': 'MULLAMURI CHARAN KUMAR', '19KB1A0136': 'MYNAMPATI JAFANYA', '19KB1A0137': 'NAGA DIVYA ',
                 '19KB1A0138': 'NALAGATLA VENKATESWARLU', '19KB1A0139': 'NALAMARI DHANUNJAY',
                 '19KB1A0141': 'NOTAM PAVITHRA ', '19KB1A0142': 'PADARTHI NITESH KUMAR',
                 '19KB1A0143': 'PALEPU YASWANTHI ', '19KB1A0144': 'PAMANJI KRISHNA MANOHAR',
                 '19KB1A0145': 'PAYASAM DHANUSH', '19KB1A0146': 'POLU SHANMUKHA PRIYA ', '19KB1A0147': 'POLUBOINA ANIL',
                 '19KB1A0148': 'POLURU MAHESH', '19KB1A0149': 'POTHURAJU LOKESH', '19KB1A0150': 'RUDRARAJU HARSHA',
                 '19KB1A0151': 'S M SAI NAVEEN', '19KB1A0153': 'SANGAM CHAITHANYA KUMAR', '19KB1A0154': 'SHAIK DAVOOD',
                 '19KB1A0155': 'SHAIK MOHID', '19KB1A0156': 'SHAIK NAYAB RASOOL', '19KB1A0157': 'SHAIK SAMEEULLA',
                 '19KB1A0158': 'SHAIK SHAHED', '19KB1A0159': 'SRIRAM RAKESH', '19KB1A0160': 'SWARNA SINDHU PRIYA ',
                 '19KB1A0161': 'SYED FAIZAN', '19KB1A0162': 'TEGACHERLA VENKATARATHNAM',
                 '19KB1A0163': 'TOPI RAJESHKUMAR', '19KB1A0164': 'TUPILI PRASANTH', '19KB1A0165': 'VAMSI KRISHNA P',
                 '19KB1A0166': 'VANIPENTA SHAIK ABDUL MUNAF', '19KB1A0167': 'VELUGOTI HEMANTH KUMAR',
                 '19KB1A0168': 'YERRABOTHU UTHEJKUMAR', '18KB1A0140': 'KUKATI SRIDHAR',
                 '19KB1A0352': 'LEKKALA CHANDRA MOHAN REDDY', '19KB1A0353': 'MADDURUPADU SUKUMAR',
                 '19KB1A0354': 'MALLELA BALACHANDRA', '19KB1A0355': 'MAMIDIPUDI HARSHAVARDHAN',
                 '19KB1A0356': 'MEDANULU SUNNITH KUMAR', '19KB1A0357': 'MUPPALA CHANDU',
                 '19KB1A0358': 'MUSUNURU SASI KUMAR', '19KB1A0359': 'NALAMALAPU PAVAN KUMAR REDDY',
                 '19KB1A0361': 'NANDIPATI SAI PRASAD', '19KB1A0362': 'PADARTHI ADITHYA REDDY',
                 '19KB1A0363': 'PALLAPU BADRI', '19KB1A0364': 'PAMULA SIVA KUMAR', '19KB1A0365': 'PANDITI NAVEEN',
                 '19KB1A0366': 'PANTA SAI SANDHEEP REDDY', '19KB1A0367': 'PANTRANGAM VENKATESH',
                 '19KB1A0368': 'PATTAN SHARUK', '19KB1A0369': 'PENAMALLI SRINADH',
                 '19KB1A0370': 'PINNABATHINA KARTHEEK', '19KB1A0371': 'POKKALI VENKATA USHA KIRAN',
                 '19KB1A0372': 'PONGURU MOHAN', '19KB1A0373': 'PONNA SRI HARSHA',
                 '19KB1A0374': 'PUCHALAPALLI PAVAN KUMAR', '19KB1A0375': 'PUJARI SAI SIVA REDDY',
                 '19KB1A0376': 'RAGIPATI BHANUPRATHAP', '19KB1A0377': 'RAMABATHINA DILEEP', '19KB1A0378': 'S MAHESH',
                 '19KB1A0379': 'SADEPALLI PRAJWAL', '19KB1A0380': 'SAKAMURI SUKUMAR',
                 '19KB1A0381': 'SANIVARAPU DINESH REDDY', '19KB1A0382': 'SANJAM MANIKANTA',
                 '19KB1A0383': 'SAYYAD NAJEER', '19KB1A0384': 'SHAIK ABBU UBED', '19KB1A0385': 'SHAIK AFZAL',
                 '19KB1A0386': 'SHAIK SHAJEED', '19KB1A0387': 'SHAIK THANWAR',
                 '19KB1A0388': 'SIRIGIRI ANIL KUMAR REDDY', '19KB1A0389': 'SYED JILANI', '19KB1A0390': 'SYED SAMAD',
                 '19KB1A0391': 'THADAKALURI VASANTH KUMAR', '19KB1A0393': 'THATIPARTHI VENKATA DATTA DARSHAN',
                 '19KB1A0394': 'THEEPALAPUDI NAGENDRA BABU', '19KB1A0395': 'THUGUTLA RAMA KRISHNA REDDY',
                 '19KB1A0396': 'TUPILI NOOTHAN REDDY', '19KB1A0397': 'UNDRALLA PRANAY KUMAR',
                 '19KB1A0398': 'UPINERTHI VIJAY KUMAR', '19KB1A0399': 'VAJARALA DEVARAJU',
                 '19KB1A03A0': 'VANGARA ACHYUTH', '19KB1A03A1': 'YANNAM MANOJ KUMAR',
                 '19KB1A03A2': 'YARRABOTHU NAGARAJU', '17KB1A03B2': 'S. VINAY', '16KB1A0335': 'G. BHANU PRAKASH',
                 '19KB1A0565': 'KARLAPUDI BHANU TEJA', '19KB1A0566': 'KARNAM NIKHITHA ',
                 '19KB1A0567': 'KARUMANCHI PRASANTH', '19KB1A0568': 'KASIM SYED ASIF',
                 '19KB1A0569': 'KATAMREDDY RUKMINI ', '19KB1A0570': 'KATTA PRANAY KUMAR', '19KB1A0571': 'KATTA SUMANTH',
                 '19KB1A0572': 'KENCHE VAISHNAVI ', '19KB1A0573': 'KETHA SRIHARSHAVARDHAN REDDY',
                 '19KB1A0574': 'KETHU SIVA CHARAN', '19KB1A0575': 'KOLLAREDDY JASWANTH', '19KB1A0576': 'KOMMI AVINASH',
                 '19KB1A0577': 'KONATHALA PALLI LIKHITHA ', '19KB1A0578': 'KONIDENA CHAITHANYA',
                 '19KB1A0579': 'KOORAPATI SAI KIRAN', '19KB1A0580': 'KOPPALA HEMA TEJASREE ',
                 '19KB1A0581': 'KOTHA NIRANJAN', '19KB1A0582': 'KRISHNA MURTHY LOKESH',
                 '19KB1A0583': 'KUDUMULA LAKSHMAMMA ', '19KB1A0584': 'LAKKU JASWITHA ',
                 '19KB1A0585': 'MAKANI KRISHNAKANTH', '19KB1A0586': 'MALEPATI DEEPTHI ',
                 '19KB1A0587': 'MALLEPULA SAI KIRAN', '19KB1A0588': 'MALLI MOUNIKA ',
                 '19KB1A0589': 'MALLIKA CHENCHAMMA ', '19KB1A0590': 'MANDAVA NITHIN', '19KB1A0591': 'MANDI HARINI ',
                 '19KB1A0592': 'MANNA MEGHASHYAM', '19KB1A0593': 'MARRI LAHARI ', '19KB1A0594': 'MAVULURU NITHIN',
                 '19KB1A0595': 'MEKALA BHUMIKA ', '19KB1A0596': 'MITTA PRANEETH KUMAR REDDY',
                 '19KB1A0597': 'MOHAMMED ADNANSAMI', '19KB1A0598': 'MOHAN KUMAR YUVA TEJA',
                 '19KB1A0599': 'MONDAM SANDHYA ', '19KB1A05A0': 'MUMMADI MALLAMMA ', '19KB1A05A1': 'MUNGARA JYOTHI ',
                 '19KB1A05A2': 'N VAMSY', '19KB1A05A3': 'NARAGANTI SUNIL KUMAR', '19KB1A05A4': 'NARAMALA AKSHITHA ',
                 '19KB1A05A5': 'NEELAM SPANDANA ', '19KB1A05A6': 'NEELI MANIKANTA', '19KB1A05A7': 'NETTAMBAKU ANUSHA ',
                 '19KB1A05A8': 'NIMMALA BALASUBRAMANYAM', '19KB1A05A9': 'ONTERU VENNELA ',
                 '19KB1A05B0': 'OTTURU DHARANI ', '19KB1A05B1': 'PACHA HEMANTH', '19KB1A05B2': 'PAIDIPULA MADHURI ',
                 '19KB1A05B3': 'PALA PRIYANKA ', '19KB1A05B4': 'PALEPU VENKATA SAI',
                 '19KB1A05B5': 'PALLE HEMANTH KUMAR REDDY', '19KB1A05B6': 'PARLAPALLI JASWANTH',
                 '19KB1A05B7': 'PARRI SRILEKHA ', '19KB1A05B8': 'PATHIPATI SREENU', '19KB1A05B9': 'PELLURU POORNIMA ',
                 '19KB1A05C0': 'PENDLIMARRI REDDYSAI VARDHAN', '19KB1A05C1': 'PETA CHARAN',
                 '19KB1A05C2': 'PITLA KRISHNA DHEERAJ', '19KB1A05C3': 'POKURU HARI CHANDANA ',
                 '19KB1A05C4': 'POLAMREDDY KOWSIK GANESH', '19KB1A05C5': 'POLU VARSHITHA ',
                 '19KB1A05C6': 'PONDHURU SAI', '19KB1A05C7': 'POORNAKANTI SAMUEL APUROOP',
                 '19KB1A05C8': 'POOSALA SAI HASINI ', '20KB5A0507': 'I. GANESH', '20KB5A0508': 'V. TEJASWINI ',
                 '20KB5A0509': 'A. VISHNU', '20KB5A0510': 'V. M. SIRISH KUMAR', '20KB5A0511': 'SHAIK. MOMIN SARDAR',
                 '20KB5A0512': 'S. SURYA', '19KB1A0465': 'KANTEPALLI CHITRANWITHA ', '19KB1A0466': 'KANUPURU NIHARIKA ',
                 '19KB1A0467': 'KARLAPUDI MANJUSHA ', '19KB1A0468': 'KASA SULEKHA ', '19KB1A0469': 'KILARI SUSMITHA ',
                 '19KB1A0470': 'KODURU SIREESHA ', '19KB1A0471': 'KONDURU SREEJA ',
                 '19KB1A0472': 'KONGATI SAI VIGHNESH', '19KB1A0473': 'KOPPU BALAJI',
                 '19KB1A0474': 'KUMBALA SANTHOSH KUMAR', '19KB1A0475': 'KUMMITHI MADHUSUDHAN REDDY',
                 '19KB1A0476': 'KUNDA VENKATESH', '19KB1A0477': 'LAGASANI NARENDRA', '19KB1A0478': 'LEKKALA NIMISHA ',
                 '19KB1A0479': 'LOKKU GOWTHAMI ', '19KB1A0480': 'MABBU LOKESH', '19KB1A0481': 'MADANA BHAVANI SANKAR',
                 '19KB1A0482': 'MADDASANI PAVAN TEJA', '19KB1A0483': 'MAHAMKALI BALAJI',
                 '19KB1A0484': 'MALEM BHARGAVI ', '19KB1A0485': 'MALLI SIREESHA ',
                 '19KB1A0486': 'MANDIPATI SREENIVASULU REDDY', '19KB1A0487': 'MAREPALLI CHAITHANYA KUMAR',
                 '19KB1A0488': 'MARRI THARUN', '19KB1A0489': 'MEKALA ALEKHYA ', '19KB1A0490': 'MEKALA SIREESHA ',
                 '19KB1A0491': 'MEKALA VAMSI', '19KB1A0492': 'MINDA MANOJ KUMAR', '19KB1A0493': 'MODDU PREM KUMAR',
                 '19KB1A0494': 'MODI PRUDHVI KESAVANADH', '19KB1A0495': 'MODIBOENA KAVYA ',
                 '19KB1A0496': 'MODIBOYINA ANKOJI', '19KB1A0497': 'MUDDULURU AKHILA ', '19KB1A0498': 'MUDI SUMANTH',
                 '19KB1A0499': 'MUKTHIPATI SUPRAJA ', '19KB1A04A0': 'MUKUNDHA USHA SREE ',
                 '19KB1A04A1': 'MUNAGALA CHAKREESH', '19KB1A04A2': 'MURA TRIVENI ', '19KB1A04A3': 'MYLAPURU BHAVANI ',
                 '19KB1A04A4': 'NAGAM SAI HARSHITHA ', '19KB1A04A5': 'NAGAREDDY KEERTHI ',
                 '19KB1A04A6': 'NAKKA SUCHARITHA ', '19KB1A04A7': 'NALLIBOINA HARI BABU',
                 '19KB1A04A8': 'NANDIMANDALAM GOWTHAMI ', '19KB1A04A9': 'NANIMELA VENKATA SATHVICK',
                 '19KB1A04B0': 'NARALA BHARGAVREDDY', '19KB1A04B1': 'NARAMALA HARSHA VARDHAN',
                 '19KB1A04B2': 'NARNE SUMANTH', '19KB1A04B3': 'NATTETI MANOJ KUMAR', '19KB1A04B4': 'NEELAM SRI RAGINI ',
                 '19KB1A04B5': 'NEELAM SUNEEL KUMAR', '19KB1A04B6': 'NIDIGUNTA JASWANTH',
                 '19KB1A04B7': 'NIJAMALA MAMATHA ', '19KB1A04B8': 'OZILI BHARGAVI PRIYA ',
                 '19KB1A04B9': 'PADAVALA ESWAR', '19KB1A04C0': 'PADI PRASANNA KUMAR',
                 '19KB1A04C1': 'PARAVASTU SRAVANI ', '19KB1A04C2': 'PEESAPATI VENKATA NAGA SUSHMA KIRAN MAI ',
                 '19KB1A04C3': 'PELLAKURU THARUNTEJA', '19KB1A04C4': 'PELLURU HEMANTH',
                 '19KB1A04C5': 'PENAGALURU SAI JIGNESH REDDY', '19KB1A04C6': 'PODAMEKALA SIVARJUNA',
                 '19KB1A04C7': 'POTHALA SAI LEELA ', '19KB1A04C8': 'PUCHALAPALLI SARVOTHAMA REDDY',
                 '20KB5A0401': 'PREM KUMAR KONISETTY', '20KB5A0402': 'P. BHUVANESWAR', '20KB5A0403': 'V. DORABABU',
                 '20KB5A0404': 'SHAIK. SHAMSHEER', '20KB5A0405': 'B. BALASRI ', '20KB5A0406': 'B. VISHNU VARDHAN REDDY',
                 '20KB5A0407': 'C. VINISHA ', '20KB5A0408': 'G. SRINIVASULU', '19KB1A0240': 'MADINENI SINDHURI ',
                 '19KB1A0241': 'MANNEMALA SUPRATHIKA ', '19KB1A0242': 'MARRI MUNI HEMA CHANDRA',
                 '19KB1A0243': 'MUDDALURU SRAVYA ', '19KB1A0245': 'NAIDU LAKSHMI CHAITHANYA',
                 '19KB1A0246': 'NAPA RATHNA KUMAR', '19KB1A0247': 'NIDIGINTI NAVYASRI ',
                 '19KB1A0248': 'PARVATHAREDDY LOKESH', '19KB1A0249': 'PASUPULETI ANUSATHWIKA ',
                 '19KB1A0250': 'PEDURU CHESVITHA ', '19KB1A0252': 'PUTHTHURU VENKATA SAI',
                 '19KB1A0253': 'PUTTAMANENI VENKATESWARLU', '19KB1A0254': 'SANKURI CHANDINI ',
                 '19KB1A0255': 'SHAIK ARSHIYA ', '19KB1A0256': 'SHAIK SUHANA AJMI ',
                 '19KB1A0257': 'SIDDAPAREDDY GOWTHAMI ', '19KB1A0258': 'SINGAMSETTY VENKATA SANDEEPNATH',
                 '19KB1A0259': 'SUNKARA PUJITHA ', '19KB1A0260': 'THIRUPATHI RAJITHA KUMARI ',
                 '19KB1A0261': 'THIRUVAIPATI SARANYA ', '19KB1A0262': 'THOPPANI HEMA ',
                 '19KB1A0263': 'THUMMA ROSHITHA ', '19KB1A0264': 'TULLURU AKHIL', '19KB1A0265': 'VALIPI ANUSHA ',
                 '19KB1A0266': 'VANJIVAKA VINEELA ', '19KB1A0267': 'VANKA RAMYASRI ',
                 '19KB1A0268': 'VARDHAGALA SRAVYA ', '19KB1A0269': 'YADDALA NIVITHA ',
                 '19KB1A0270': 'YADDALAPUDI REKHA ', '19KB1A0271': 'YAKASIRI PADMA ',
                 '19KB1A0272': 'YANAMALA PENCHALAREDDY', '19KB1A0273': 'YARASI VIVEK',
                 '19KB1A0274': 'YARRAMAKA SUSMITHA ', '19KB1A0275': 'YEARUVA SRINATH REDDY',
                 '19KB1A0276': 'YERRABOTHU SOWRYA', '20KB5A0222': 'B. ARAVIND', '20KB5A0223': 'P. SIVA GOWRI ',
                 '20KB5A0224': 'D. MANOJ', '20KB5A0225': 'D. MAHA LAKSHMI ', '20KB5A0226': 'B. MURALI KRISHNA',
                 '20KB5A0227': 'M. CHANDRIKA ', '20KB5A0228': 'A. HARSHAVARDHAN', '20KB5A0229': 'SHAIK. VASEEM AKRAM',
                 '20KB5A0230': 'D. NAVEEN', '20KB5A0231': 'G. JAYAKRISHNA', '20KB5A0232': 'M. DEVI',
                 '20KB5A0233': 'C. SURESH KUMAR', '20KB5A0234': 'N. DILLI BABU', '20KB5A0235': 'M. SUPRAJA ',
                 '20KB5A0236': 'D. VYSHNAVI ', '20KB5A0237': 'B. NISHITHA ', '20KB5A0238': 'D. PALLAVI ',
                 '20KB5A0239': 'T. MAMATHA MURALI ', '20KB5A0240': 'C. SANTHOSH', '20KB5A0241': 'N. VENKATA HARSHA',
                 '20KB5A0242': 'SHAIK. MOHSEEN AHAMAD', '18KB5A0202': 'BANDI VENKATAKISHORE REDDY',
                 '20KB5A0101': 'R. SUNAYANA ', '20KB5A0102': 'E. SIVA GANESH', '20KB5A0103': 'S. HEMANTH KUMAR',
                 '20KB5A0104': 'G. PAVAN KALYAN', '20KB5A0105': 'K. NAVEEN', '20KB5A0106': 'K. GURUKRISHNA',
                 '20KB5A0107': 'S. SUDHEER', '20KB5A0108': 'M. SURENDRA', '20KB5A0109': 'I. PARDHASARADHI',
                 '20KB5A0110': 'T. SRAVAN KRISHNA', '20KB5A0111': 'SYED. MUHEEB', '20KB5A0112': 'M. SAI KRISHNA',
                 '20KB5A0113': 'M. MOHAN CHAND', '20KB5A0114': 'R. VENKATA MANOJ', '20KB5A0115': 'V. JAYARAJU',
                 '20KB5A0116': 'M. ANIL', '20KB5A0117': 'U. SRIRAM DIWAKAR', '20KB5A0118': 'K. SUDHARSHAN',
                 '20KB5A0119': 'K. MOUNIKA ', '20KB5A0120': 'M. VINOD', '20KB5A0121': 'G. SAMPATHKUMAR',
                 '20KB5A0122': 'G. KAVYA ', '20KB5A0123': 'S. YASWANTH', '20KB5A0124': 'K. JAYA PRAKASH',
                 '20KB5A0125': 'R. SAMPATH KUMAR', '20KB5A0126': 'G. NAVEEN', '20KB5A0127': 'M. SAI BHARATH',
                 '20KB5A0128': 'V. NANDINI ', '20KB5A0129': 'E. SATHISH KUMAR', '20KB5A0130': 'B. VIJAY KUMAR',
                 '20KB5A0131': 'C. JNANESWAR', '20KB5A0132': 'M. SUNIL KUMAR REDDY', '20KB5A0133': 'M. MANJULA ',
                 '20KB5A0134': 'A. SIVA KRISHNA', '20KB5A0135': 'V. RAJA SEKHAR', '20KB5A0136': 'M. SURENDRA',
                 '20KB5A0137': 'K. BHARATH', '20KB5A0138': 'S. AVINASH REDDY', '20KB5A0139': 'R. PAVANKUMAR',
                 '20KB5A0140': 'U. RAVITEJA', '20KB5A0141': 'R. LOHITH NIKHIL', '20KB5A0142': 'SHAIK. RIYAZ',
                 '20KB5A0143': 'O. BHARATH', '20KB5A0144': 'CH. SANTHOSH', '20KB5A0145': 'G. SUBBARAYUDU',
                 '20KB5A0146': 'SYED. KHUTHUBULLA', '20KB5A0147': 'B. SEENU', '18KB1A0124': 'ERIBOYINA SUBRAMANYAM',
                 '18KB1A0127': 'GOLLAPALEM GOWTHAM', '20KB5A0301': 'S. SUJITH', '20KB5A0302': 'M. SUBASH',
                 '20KB5A0303': 'G. HARSHAVARDHAN', '20KB5A0304': 'C. AADARSH', '20KB5A0305': 'K. CHETHAN SAI',
                 '20KB5A0306': 'K. NAVEEN', '20KB5A0307': 'K. NAVEEN', '20KB5A0308': 'U. SANDEEP',
                 '20KB5A0309': 'SYED. ALEEM', '20KB5A0310': 'P. MANOJ', '20KB5A0311': 'V. BHARATH RAJ',
                 '20KB5A0312': 'N. PAVAN', '20KB5A0313': 'S. VIKAS', '20KB5A0314': 'SHAIK. NAVEED',
                 '20KB5A0315': 'L. SIVA KUMAR', '20KB5A0316': 'V. SAISANKAR', '20KB5A0317': 'V. SHARATH KUMAR',
                 '20KB5A0318': 'K. UDAYKIRAN', '20KB5A0319': 'P. DAVOD', '20KB5A0320': 'U. ANVESH',
                 '20KB5A0321': 'SHAIK. JALEEL', '20KB5A0322': 'M. SIVAKUMAR', '20KB5A0323': 'V. NEELESH',
                 '20KB5A0324': 'SHAIK. MANSOOR', '20KB5A0325': 'T. VENKATA SAI', '20KB5A0326': 'T. VENKATESH',
                 '20KB5A0327': 'C. VINAY KUMAR', '20KB5A0328': 'G. USHODAY', '20KB5A0329': 'V. RAKESH',
                 '20KB5A0330': 'C. VENKATESWARLU', '20KB5A0331': 'K. BHARGAV', '20KB5A0332': 'T. ESWARSARATHCHANDRA',
                 '20KB5A0333': 'K. BHARATH CHANDRA', '20KB5A0334': 'C. BHANUCHANDU',
                 '20KB5A0335': 'SHAIK. MASTHAN BASHA', '20KB5A0336': 'S. JAGADEESH KUMAR', '20KB5A0337': 'B. PRAKASH',
                 '20KB5A0338': 'A. RAKESH', '20KB5A0339': 'C. VINEETH', '20KB5A0340': 'B. PRASAD KUMAR',
                 '20KB5A0341': 'M. SAI MANOJ', '20KB5A0342': 'S. BOINA HARI', '20KB5A0343': 'K. KOTESWAR',
                 '20KB5A0344': 'R. VENKATA SAI', '20KB5A0345': 'A. MUNI HARSHA VARDHAN', '20KB5A0346': 'C. JITHENDRA',
                 '20KB5A0347': 'B. SREENU', '20KB5A0348': 'P. MUNI SYAM', '20KB5A0349': 'N. VENKATA VAMSIKRISHNA',
                 '20KB5A0350': 'G. GIRISH REDDY', '20KB5A0351': 'K. SWETHA ', '20KB5A0352': 'SHAIK. ASIF',
                 '20KB5A0353': 'M. ASHOK REDDY', '20KB5A0354': 'L. SREEKANTH', '20KB5A0356': 'T. GOKUL',
                 '20KB5A0357': 'K. SAI BALA', '20KB5A0358': 'SHAIK. SAJID', '20KB5A0359': 'SHAIK. LATHIF',
                 '20KB5A0360': 'K. YASWANTH', '20KB5A0362': 'B. VENKATESH', '20KB5A0363': 'V. SAI KRISHNA',
                 '20KB5A0364': 'P. ABHIRAM', '20KB5A0365': 'N. MANJUNATH', '20KB5A0366': 'M. PURUSHOTHAM',
                 '20KB5A0367': 'SHAIK. MAHAMMAD RAFI', '20KB5A0368': 'T. SOHITH REDDY', '20KB5A0370': 'P. SUDHEER',
                 '20KB5A0371': 'G. SAI JASWANTH', '20KB5A0372': 'K. KIRAN', '19KB1A05C9': 'PUDI GANESH REDDY',
                 '19KB1A05D0': 'PUSALA BHANUSREE SAIRAJI ', '19KB1A05D1': 'RAGALA SRIHARI',
                 '19KB1A05D2': 'RAMABATTINA SOMADHARA ', '19KB1A05D3': 'RAMIREDDY GANESH GOPAL REDDY',
                 '19KB1A05D4': 'RAMISETTI PRASANTH', '19KB1A05D5': 'RATAKONDA SRI CHANDANA ',
                 '19KB1A05D6': 'RAVULA MANOZ KUMAR', '19KB1A05D7': 'RAYAPU ADITHYA', '19KB1A05D8': 'RENANGI VENU',
                 '19KB1A05D9': 'RENDLA RAJESWARI ', '19KB1A05E0': 'REVUNURU SAKETH REDDY',
                 '19KB1A05E1': 'SADANALA SAI HARISH', '19KB1A05E2': 'SAIKRISHNA BINKINA',
                 '19KB1A05E3': 'SAMIDIBOINA GANESH', '19KB1A05E4': 'SANAMBATLA LIKHITHA ',
                 '19KB1A05E5': 'SANGARAJU NEETHU ', '19KB1A05E6': 'SANNAYI SONY ANUPAMA ',
                 '19KB1A05E7': 'SETTY NAVEEN KUMAR', '19KB1A05E8': 'SHAIK AFZAL', '19KB1A05E9': 'SHAIK FARAHANA ',
                 '19KB1A05F0': 'SHAIK JASMINE ', '19KB1A05F1': 'SHAIK MUSTHAK AHMAD',
                 '19KB1A05F2': 'SHAIK PALUR SAMEENA ', '19KB1A05F3': 'SHAIK SHABNA BANU ',
                 '19KB1A05F4': 'SHAIK SHAKEER', '19KB1A05F5': 'SHAIK THASMIYA ', '19KB1A05F6': 'SHAIK YAKHOOB',
                 '19KB1A05F7': 'SINGANAPALLI UDAY KUMAR', '19KB1A05F8': 'SOLLETI TEJASWINI ',
                 '19KB1A05F9': 'SUNKARA PAVANKUMAR', '19KB1A05G0': 'SYED AFZAL', '19KB1A05G1': 'TALAHARI CHAITANYA ',
                 '19KB1A05G2': 'TELAGANENI ADITHYA', '19KB1A05G3': 'THATIBOINA MAHESWARI ',
                 '19KB1A05G4': 'THATIPARTHI PENCHALA PRASANNA ', '19KB1A05G5': 'THATIPARTHI VENKATA SAI SMARAN',
                 '19KB1A05G6': 'THIMMALAPURAM CHARAN KUMAR', '19KB1A05G7': 'THOTA SAHITHI ',
                 '19KB1A05G8': 'THUPILI VENKATA PRASANNA ', '19KB1A05G9': 'THURIMERLA MALLI KARJUNA REDDY',
                 '19KB1A05H0': 'V GAYATHRI ', '19KB1A05H1': 'VALLAMETI AARTHI ', '19KB1A05H2': 'VALLURU HEMA KUMARI ',
                 '19KB1A05H3': 'VALLURU SUSHWANTH KUMAR', '19KB1A05H4': 'VANNE PRASAD',
                 '19KB1A05H5': 'VARIKUTI OBULREDDY', '19KB1A05H6': 'VEERANNAGARI VINOD KUMAR',
                 '19KB1A05H7': 'VELIGARAM LATHA ', '19KB1A05H8': 'VELURU JOSHI',
                 '19KB1A05H9': 'VEMIREDDY VENKATA SATYANARAYANA REDDY', '19KB1A05I0': 'VEMMALETI BHAVANA ',
                 '19KB1A05I1': 'VEMPALLA SUNEEL KUMAR', '19KB1A05I2': 'VENUMBAKA DHARANI ',
                 '19KB1A05I3': 'VETTI SRUTHI ', '19KB1A05I4': 'VOGGU SAI GEETHIKA ', '19KB1A05I5': 'WILLIAM KEERTHANA ',
                 '19KB1A05I6': 'YADATI HARSHITHA ', '19KB1A05I7': 'YADDALA SIMHIKA REDDY ',
                 '19KB1A05I8': 'YALAMARTHI YAGNA PRASANNA KUMAR', '19KB1A05I9': 'YANATI RAJANIVAS',
                 '19KB1A05J0': 'YARLAGADDA SRIKAR', '19KB1A05J1': 'YELLASIRI HARSHITHA ',
                 '19KB1A05J2': 'YELLASIRI MADHUSMITHA ', '19KB1A05J3': 'YERRA JAGADEESH', '20KB5A0513': 'P. JAHNAVI ',
                 '20KB5A0514': 'N. KUMAR', '20KB5A0515': 'K. RESHMA ', '20KB5A0516': 'T. SURESH',
                 '20KB5A0517': 'B. VIJAY KUMAR', '20KB5A0518': 'A. VENKATESWARLU', '19KB1A04C9': 'PULLITHU HARIKA ',
                 '19KB1A04D0': 'PUNURU JITHENDRA REDDY', '19KB1A04D1': 'RACHAMALLI SRAVANI ',
                 '19KB1A04D2': 'RAJA DORASANAMMA ', '19KB1A04D3': 'RAJAVELA PAVAN KUMAR',
                 '19KB1A04D4': 'RAMISETTY KUMAR', '19KB1A04D5': 'RANGASAMY KAVYA', '19KB1A04D6': 'RAO HARI KRISHNA',
                 '19KB1A04D7': 'RAVI HARSHA VARDHAN REDDY', '19KB1A04D8': 'REDDY SUDHEER',
                 '19KB1A04D9': 'REMALA THEJASWINI ', '19KB1A04E0': 'SAKAM NARENDRA', '19KB1A04E1': 'SALLA CHENNAIAH',
                 '19KB1A04E2': 'SAMREEN SHAIK ', '19KB1A04E3': 'SAPRAM UPENDRA', '19KB1A04E4': 'SARANGAM MANINDRA',
                 '19KB1A04E5': 'SARANGAM SATHWIK', '19KB1A04E6': 'SEKHAPURAM PRADEEP KUMAR',
                 '19KB1A04E7': 'SHAIK ABDUL RAQIB', '19KB1A04E9': 'SHAIK ASLAM', '19KB1A04F0': 'SHAIK HABEEBUNNISA ',
                 '19KB1A04F1': 'SHAIK JAVEED', '19KB1A04F2': 'SHAIK NAZMA ', '19KB1A04F3': 'SHAIK RIJWANA ',
                 '19KB1A04F4': 'SHAIK SADHIKA YASEEN ', '19KB1A04F5': 'SHAIK SALMAN BASHA',
                 '19KB1A04F6': 'SHAIK SHAHISTHA ', '19KB1A04F7': 'SHAIK SUMAYA ',
                 '19KB1A04F8': 'SIDDAVATAM JAGADISHWARA REDDY', '19KB1A04F9': 'SIMHADRI SAI SINDHU ',
                 '19KB1A04G0': 'SINGARAPU SURESH REDDY', '19KB1A04G1': 'SOMISETTY VENKATA SIVA SAI PRASANTH',
                 '19KB1A04G2': 'SUNNAPU VANDANA ', '19KB1A04G3': 'SUSARLA HEMANTH', '19KB1A04G4': 'SUSARLA LIKITHA ',
                 '19KB1A04G5': 'SYED SHAHIN ', '19KB1A04G6': 'TAMBABATHINA SAIKRISHNA',
                 '19KB1A04G7': 'THADIPIREDDY SAI DINESH REDDY', '19KB1A04G8': 'THAMBI DEVENDRA BABU',
                 '19KB1A04G9': 'THEEPALAPUDI NARENDRA', '19KB1A04H0': 'THIRUMURU JYOTHSNA ',
                 '19KB1A04H1': 'THOTA MANEIAH', '19KB1A04H2': 'THUMMALA PRANATHI ', '19KB1A04H3': 'TIRUVEDI TEJASWINI ',
                 '19KB1A04H4': 'TUNGA DINESH', '19KB1A04H5': 'UBBARAPU BRAHMA RAJA',
                 '19KB1A04H6': 'ULLIPAYALA HARI KRISHNA', '19KB1A04H7': 'VAJJA SUNEEL',
                 '19KB1A04H8': 'VARADARAJU HARSHAVARDHAN', '19KB1A04H9': 'VARDINENI POORNIMA ',
                 '19KB1A04I0': 'VARIKELA PENCHALAIAH', '19KB1A04I1': 'VAYYALA SAI SANDEEP',
                 '19KB1A04I2': 'VELUGU LATHA ', '19KB1A04I3': 'VEMULACHEDU SAI VINOOTHNA ',
                 '19KB1A04I4': 'VEPAKULA SARADHI', '19KB1A04I5': 'VIBHUDI ARCHANA ',
                 '19KB1A04I6': 'VINUKONDA PENCHALA PRASAD', '19KB1A04I7': 'YACHAMANENI DEDEEPYA ',
                 '19KB1A04I8': 'YARATI SUSHMA ', '19KB1A04I9': 'YARRABATHINA BHARATH KUMAR',
                 '19KB1A04J0': 'YARRAMATHI AMRUTHA ', '19KB1A04J1': 'YATTAPU BHANU PRAKASH',
                 '19KB1A04J3': 'YERRA SIVA KISHOR', '20KB5A0410': 'C. DHARANI ', '20KB5A0411': 'P. THARUN KUMAR',
                 '20KB5A0412': 'I. SASIKIRANMAI ', '20KB5A0413': 'D. MUDDU KRISHNA', '20KB5A0414': 'V. MADHAVA',
                 '20KB5A0415': 'V. RAMA DEVI ', '20KB5A0416': 'P. HEMANTHKUMAR', '20KB5A0417': 'V. TEJESWAR REDDY',
                 '20KB5A0418': 'K. VIJITHA '}
student_data = {'21KB1A0301': '3 1 1', '21KB1A0302': '3 1 1', '21KB1A0303': '3 1 1', '21KB1A0304': '3 1 1',
                '21KB1A0305': '3 1 1', '21KB1A0306': '3 1 1', '21KB1A0307': '3 1 1', '21KB1A0308': '3 1 1',
                '21KB1A0309': '3 1 1', '21KB1A0310': '3 1 1', '21KB1A0311': '3 1 1', '21KB1A0312': '3 1 1',
                '21KB1A0313': '3 1 1', '21KB1A0314': '3 1 1', '21KB1A0315': '3 1 1', '21KB1A0316': '3 1 1',
                '21KB1A0317': '3 1 1', '21KB1A0318': '3 1 1', '21KB1A0319': '3 1 1', '21KB1A0320': '3 1 1',
                '21KB1A0321': '3 1 1', '21KB1A0322': '3 1 1', '21KB1A0323': '3 1 1', '21KB1A0324': '3 1 1',
                '21KB1A0325': '3 1 1', '21KB1A0326': '3 1 1', '21KB1A0327': '3 1 1', '21KB1A0328': '3 1 1',
                '21KB1A0329': '3 1 1', '21KB1A0330': '3 1 1', '21KB1A0331': '3 1 1', '21KB1A0332': '3 1 1',
                '21KB1A0333': '3 1 1', '21KB1A0334': '3 1 1', '21KB1A0335': '3 1 1', '21KB1A0336': '3 1 1',
                '21KB1A0337': '3 1 1', '21KB1A0338': '3 1 1', '21KB1A0339': '3 1 1', '21KB1A0340': '3 1 1',
                '21KB1A0341': '3 1 1', '21KB1A0342': '3 1 1', '21KB1A0343': '3 1 1', '21KB1A0344': '3 1 1',
                '21KB1A0345': '3 1 1', '21KB1A0346': '3 1 1', '21KB1A0347': '3 1 1', '21KB1A0348': '3 1 1',
                '21KB1A0349': '3 1 1', '21KB1A0350': '3 1 1', '21KB1A0351': '3 1 1', '21KB1A0352': '3 1 1',
                '21KB1A0353': '3 1 1', '21KB1A0501': '3 2 2', '21KB1A0502': '3 2 2', '21KB1A0503': '3 2 2',
                '21KB1A0504': '3 2 2', '21KB1A0505': '3 2 2', '21KB1A0506': '3 2 2', '21KB1A0507': '3 2 2',
                '21KB1A0508': '3 2 2', '21KB1A0509': '3 2 2', '21KB1A0510': '3 2 2', '21KB1A0511': '3 2 2',
                '21KB1A0512': '3 2 2', '21KB1A0513': '3 2 2', '21KB1A0514': '3 2 2', '21KB1A0515': '3 2 2',
                '21KB1A0516': '3 2 2', '21KB1A0517': '3 2 2', '21KB1A0518': '3 2 2', '21KB1A0519': '3 2 2',
                '21KB1A0520': '3 2 2', '21KB1A0521': '3 2 2', '21KB1A0522': '3 2 2', '21KB1A0523': '3 2 2',
                '21KB1A0524': '3 2 2', '21KB1A0525': '3 2 2', '21KB1A0526': '3 2 2', '21KB1A0527': '3 2 2',
                '21KB1A0528': '3 2 2', '21KB1A0529': '3 2 2', '21KB1A0530': '3 2 2', '21KB1A0531': '3 2 2',
                '21KB1A0532': '3 2 2', '21KB1A0533': '3 2 2', '21KB1A0534': '3 2 2', '21KB1A0535': '3 2 2',
                '21KB1A0536': '3 2 2', '21KB1A0537': '3 2 2', '21KB1A0538': '3 2 2', '21KB1A0539': '3 2 2',
                '21KB1A0540': '3 2 2', '21KB1A0541': '3 2 2', '21KB1A0542': '3 2 2', '21KB1A0543': '3 2 2',
                '21KB1A0544': '3 2 2', '21KB1A0545': '3 2 2', '21KB1A0546': '3 2 2', '21KB1A0547': '3 2 2',
                '21KB1A0548': '3 2 2', '21KB1A0549': '3 2 2', '21KB1A0550': '3 2 2', '21KB1A0551': '3 2 2',
                '21KB1A0552': '3 2 2', '21KB1A0553': '3 2 2', '21KB1A0554': '3 2 2', '21KB1A0555': '3 2 2',
                '21KB1A0556': '3 2 2', '21KB1A0557': '3 2 2', '21KB1A0558': '3 2 2', '21KB1A0559': '3 2 2',
                '21KB1A0560': '3 2 2', '21KB1A0561': '3 2 2', '21KB1A0562': '3 2 2', '21KB1A0563': '3 2 2',
                '21KB1A0564': '3 2 2', '21KB1A0565': '3 2 2', '21KB1A0566': '3 2 2', '21KB1A0567': '3 2 3',
                '21KB1A0568': '3 2 3', '21KB1A0569': '3 2 3', '21KB1A0570': '3 2 3', '21KB1A0571': '3 2 3',
                '21KB1A0572': '3 2 3', '21KB1A0573': '3 2 3', '21KB1A0574': '3 2 3', '21KB1A0575': '3 2 3',
                '21KB1A0576': '3 2 3', '21KB1A0577': '3 2 3', '21KB1A0578': '3 2 3', '21KB1A0579': '3 2 3',
                '21KB1A0580': '3 2 3', '21KB1A0581': '3 2 3', '21KB1A0582': '3 2 3', '21KB1A0583': '3 2 3',
                '21KB1A0584': '3 2 3', '21KB1A0585': '3 2 3', '21KB1A0586': '3 2 3', '21KB1A0587': '3 2 3',
                '21KB1A0588': '3 2 3', '21KB1A0589': '3 2 3', '21KB1A0590': '3 2 3', '21KB1A0591': '3 2 3',
                '21KB1A0592': '3 2 3', '21KB1A0593': '3 2 3', '21KB1A0594': '3 2 3', '21KB1A0595': '3 2 3',
                '21KB1A0596': '3 2 3', '21KB1A0597': '3 2 3', '21KB1A0598': '3 2 3', '21KB1A0599': '3 2 3',
                '21KB1A05A0': '3 2 3', '21KB1A05A1': '3 2 3', '21KB1A05A2': '3 2 3', '21KB1A05A3': '3 2 3',
                '21KB1A05A4': '3 2 3', '21KB1A05A5': '3 2 3', '21KB1A05A6': '3 2 3', '21KB1A05A7': '3 2 3',
                '21KB1A05A8': '3 2 3', '21KB1A05A9': '3 2 3', '21KB1A05B0': '3 2 3', '21KB1A05B1': '3 2 3',
                '21KB1A05B2': '3 2 3', '21KB1A05B3': '3 2 3', '21KB1A05B4': '3 2 3', '21KB1A05B5': '3 2 3',
                '21KB1A05B6': '3 2 3', '21KB1A05B7': '3 2 3', '21KB1A05B8': '3 2 3', '21KB1A05B9': '3 2 3',
                '21KB1A05C0': '3 2 3', '21KB1A05C1': '3 2 3', '21KB1A05C2': '3 2 3', '21KB1A05C3': '3 2 3',
                '21KB1A05C4': '3 2 3', '21KB1A05C5': '3 2 3', '21KB1A05C6': '3 2 3', '21KB1A05C7': '3 2 3',
                '21KB1A05C8': '3 2 3', '21KB1A05C9': '3 2 3', '21KB1A05D0': '3 2 3', '21KB1A05D1': '3 2 3',
                '21KB1A05D2': '3 2 3', '21KB1A05D3': '3 2 4', '21KB1A05D4': '3 2 4', '21KB1A05D5': '3 2 4',
                '21KB1A05D6': '3 2 4', '21KB1A05D7': '3 2 4', '21KB1A05D8': '3 2 4', '21KB1A05D9': '3 2 4',
                '21KB1A05E0': '3 2 4', '21KB1A05E1': '3 2 4', '21KB1A05E2': '3 2 4', '21KB1A05E3': '3 2 4',
                '21KB1A05E4': '3 2 4', '21KB1A05E5': '3 2 4', '21KB1A05E6': '3 2 4', '21KB1A05E7': '3 2 4',
                '21KB1A05E8': '3 2 4', '21KB1A05E9': '3 2 4', '21KB1A05F0': '3 2 4', '21KB1A05F1': '3 2 4',
                '21KB1A05F2': '3 2 4', '21KB1A05F3': '3 2 4', '21KB1A05F4': '3 2 4', '21KB1A05F5': '3 2 4',
                '21KB1A05F6': '3 2 4', '21KB1A05F7': '3 2 4', '21KB1A05F8': '3 2 4', '21KB1A05F9': '3 2 4',
                '21KB1A05G0': '3 2 4', '21KB1A05G1': '3 2 4', '21KB1A05G2': '3 2 4', '21KB1A05G3': '3 2 4',
                '21KB1A05G4': '3 2 4', '21KB1A05G5': '3 2 4', '21KB1A05G6': '3 2 4', '21KB1A05G7': '3 2 4',
                '21KB1A05G8': '3 2 4', '21KB1A05G9': '3 2 4', '21KB1A05H0': '3 2 4', '21KB1A05H1': '3 2 4',
                '21KB1A05H2': '3 2 4', '21KB1A05H3': '3 2 4', '21KB1A05H4': '3 2 4', '21KB1A05H5': '3 2 4',
                '21KB1A05H6': '3 2 4', '21KB1A05H7': '3 2 4', '21KB1A05H8': '3 2 4', '21KB1A05H9': '3 2 4',
                '21KB1A05I0': '3 2 4', '21KB1A05I1': '3 2 4', '21KB1A05I2': '3 2 4', '21KB1A05I3': '3 2 4',
                '21KB1A05I4': '3 2 4', '21KB1A05I5': '3 2 4', '21KB1A05I6': '3 2 4', '21KB1A05I7': '3 2 4',
                '21KB1A05I8': '3 2 4', '21KB1A05I9': '3 2 4', '21KB1A05J0': '3 2 4', '21KB1A05J1': '3 2 4',
                '21KB1A05J2': '3 2 4', '21KB1A05J3': '3 2 4', '21KB1A05J4': '3 2 4', '21KB1A05J5': '3 2 4',
                '21KB1A05J6': '3 2 4', '21KB1A05J7': '3 2 4', '21KB1A05J8': '3 2 4', '21KB1A0401': '3 3 2',
                '21KB1A0402': '3 3 2', '21KB1A0403': '3 3 2', '21KB1A0404': '3 3 2', '21KB1A0405': '3 3 2',
                '21KB1A0406': '3 3 2', '21KB1A0407': '3 3 2', '21KB1A0408': '3 3 2', '21KB1A0409': '3 3 2',
                '21KB1A0410': '3 3 2', '21KB1A0411': '3 3 2', '21KB1A0412': '3 3 2', '21KB1A0413': '3 3 2',
                '21KB1A0414': '3 3 2', '21KB1A0415': '3 3 2', '21KB1A0416': '3 3 2', '21KB1A0417': '3 3 2',
                '21KB1A0418': '3 3 2', '21KB1A0419': '3 3 2', '21KB1A0420': '3 3 2', '21KB1A0421': '3 3 2',
                '21KB1A0422': '3 3 2', '21KB1A0423': '3 3 2', '21KB1A0424': '3 3 2', '21KB1A0425': '3 3 2',
                '21KB1A0426': '3 3 2', '21KB1A0427': '3 3 2', '21KB1A0428': '3 3 2', '21KB1A0429': '3 3 2',
                '21KB1A0430': '3 3 2', '21KB1A0431': '3 3 2', '21KB1A0432': '3 3 2', '21KB1A0433': '3 3 2',
                '21KB1A0434': '3 3 2', '21KB1A0435': '3 3 2', '21KB1A0436': '3 3 2', '21KB1A0437': '3 3 2',
                '21KB1A0438': '3 3 2', '21KB1A0439': '3 3 2', '21KB1A0440': '3 3 2', '21KB1A0441': '3 3 2',
                '21KB1A0442': '3 3 2', '21KB1A0443': '3 3 2', '21KB1A0444': '3 3 2', '21KB1A0445': '3 3 2',
                '21KB1A0446': '3 3 2', '21KB1A0447': '3 3 2', '21KB1A0448': '3 3 2', '21KB1A0449': '3 3 2',
                '21KB1A0450': '3 3 2', '21KB1A0451': '3 3 2', '21KB1A0452': '3 3 2', '21KB1A0453': '3 3 2',
                '21KB1A0454': '3 3 2', '21KB1A0455': '3 3 2', '21KB1A0456': '3 3 2', '21KB1A0457': '3 3 2',
                '21KB1A0458': '3 3 3', '21KB1A0459': '3 3 3', '21KB1A0460': '3 3 3', '21KB1A0461': '3 3 3',
                '21KB1A0462': '3 3 3', '21KB1A0463': '3 3 3', '21KB1A0464': '3 3 3', '21KB1A0465': '3 3 3',
                '21KB1A0466': '3 3 3', '21KB1A0467': '3 3 3', '21KB1A0468': '3 3 3', '21KB1A0469': '3 3 3',
                '21KB1A0470': '3 3 3', '21KB1A0471': '3 3 3', '21KB1A0472': '3 3 3', '21KB1A0473': '3 3 3',
                '21KB1A0474': '3 3 3', '21KB1A0475': '3 3 3', '21KB1A0476': '3 3 3', '21KB1A0477': '3 3 3',
                '21KB1A0478': '3 3 3', '21KB1A0479': '3 3 3', '21KB1A0480': '3 3 3', '21KB1A0481': '3 3 3',
                '21KB1A0482': '3 3 3', '21KB1A0483': '3 3 3', '21KB1A0484': '3 3 3', '21KB1A0485': '3 3 3',
                '21KB1A0486': '3 3 3', '21KB1A0487': '3 3 3', '21KB1A0488': '3 3 3', '21KB1A0489': '3 3 3',
                '21KB1A0490': '3 3 3', '21KB1A0491': '3 3 3', '21KB1A0492': '3 3 3', '21KB1A0493': '3 3 3',
                '21KB1A0494': '3 3 3', '21KB1A0495': '3 3 3', '21KB1A0496': '3 3 3', '21KB1A0497': '3 3 3',
                '21KB1A0498': '3 3 3', '21KB1A0499': '3 3 3', '21KB1A04A0': '3 3 3', '21KB1A04A1': '3 3 3',
                '21KB1A04A2': '3 3 3', '21KB1A04A3': '3 3 3', '21KB1A04A4': '3 3 3', '21KB1A04A5': '3 3 3',
                '21KB1A04A6': '3 3 3', '21KB1A04A7': '3 3 3', '21KB1A04A8': '3 3 3', '21KB1A04A9': '3 3 3',
                '21KB1A04B0': '3 3 3', '21KB1A04B1': '3 3 3', '21KB1A04B2': '3 3 3', '21KB1A04B3': '3 3 3',
                '21KB1A04B4': '3 3 3', '21KB1A04B5': '3 3 4', '21KB1A04B6': '3 3 4', '21KB1A04B7': '3 3 4',
                '21KB1A04B8': '3 3 4', '21KB1A04B9': '3 3 4', '21KB1A04C0': '3 3 4', '21KB1A04C1': '3 3 4',
                '21KB1A04C2': '3 3 4', '21KB1A04C3': '3 3 4', '21KB1A04C4': '3 3 4', '21KB1A04C5': '3 3 4',
                '21KB1A04C6': '3 3 4', '21KB1A04C7': '3 3 4', '21KB1A04C8': '3 3 4', '21KB1A04C9': '3 3 4',
                '21KB1A04D0': '3 3 4', '21KB1A04D1': '3 3 4', '21KB1A04D2': '3 3 4', '21KB1A04D3': '3 3 4',
                '21KB1A04D4': '3 3 4', '21KB1A04D5': '3 3 4', '21KB1A04D6': '3 3 4', '21KB1A04D7': '3 3 4',
                '21KB1A04D8': '3 3 4', '21KB1A04D9': '3 3 4', '21KB1A04E0': '3 3 4', '21KB1A04E1': '3 3 4',
                '21KB1A04E2': '3 3 4', '21KB1A04E3': '3 3 4', '21KB1A04E4': '3 3 4', '21KB1A04E5': '3 3 4',
                '21KB1A04E6': '3 3 4', '21KB1A04E7': '3 3 4', '21KB1A04E8': '3 3 4', '21KB1A04E9': '3 3 4',
                '21KB1A04F0': '3 3 4', '21KB1A04F1': '3 3 4', '21KB1A04F2': '3 3 4', '21KB1A04F3': '3 3 4',
                '21KB1A04F4': '3 3 4', '21KB1A04F5': '3 3 4', '21KB1A04F6': '3 3 4', '21KB1A04F7': '3 3 4',
                '21KB1A04F9': '3 3 4', '21KB1A04G0': '3 3 4', '21KB1A04G1': '3 3 4', '21KB1A04G2': '3 3 4',
                '21KB1A04G3': '3 3 4', '21KB1A04G4': '3 3 4', '21KB1A04G5': '3 3 4', '21KB1A04G6': '3 3 4',
                '21KB1A04G7': '3 3 4', '21KB1A04G8': '3 3 4', '21KB1A04G9': '3 3 4', '21KB1A04H0': '3 3 4',
                '21KB1A04H1': '3 3 4', '21KB1A04H2': '3 3 4', '21KB1A0201': '3 4 2', '21KB1A0202': '3 4 2',
                '21KB1A0203': '3 4 2', '21KB1A0204': '3 4 2', '21KB1A0205': '3 4 2', '21KB1A0206': '3 4 2',
                '21KB1A0207': '3 4 2', '21KB1A0208': '3 4 2', '21KB1A0209': '3 4 2', '21KB1A0210': '3 4 2',
                '21KB1A0211': '3 4 2', '21KB1A0212': '3 4 2', '21KB1A0213': '3 4 2', '21KB1A0214': '3 4 2',
                '21KB1A0215': '3 4 2', '21KB1A0216': '3 4 2', '21KB1A0217': '3 4 2', '21KB1A0218': '3 4 2',
                '21KB1A0219': '3 4 2', '21KB1A0220': '3 4 2', '21KB1A0221': '3 4 2', '21KB1A0222': '3 4 2',
                '21KB1A0223': '3 4 2', '21KB1A0224': '3 4 2', '21KB1A0225': '3 4 2', '21KB1A0226': '3 4 2',
                '21KB1A0227': '3 4 2', '21KB1A0228': '3 4 2', '21KB1A0229': '3 4 2', '21KB1A0230': '3 4 2',
                '21KB1A0231': '3 4 2', '21KB1A0232': '3 4 2', '21KB1A0233': '3 4 2', '21KB1A0234': '3 4 2',
                '21KB1A0235': '3 4 2', '21KB1A0236': '3 4 2', '21KB1A0237': '3 4 2', '21KB1A0238': '3 4 2',
                '21KB1A0239': '3 4 2', '21KB1A0240': '3 4 2', '21KB1A0241': '3 4 2', '21KB1A0242': '3 4 2',
                '21KB1A0243': '3 4 2', '21KB1A0244': '3 4 2', '21KB1A0245': '3 4 2', '21KB1A0246': '3 4 2',
                '21KB1A0247': '3 4 2', '21KB1A0248': '3 4 3', '21KB1A0249': '3 4 3', '21KB1A0250': '3 4 3',
                '21KB1A0251': '3 4 3', '21KB1A0252': '3 4 3', '21KB1A0253': '3 4 3', '21KB1A0254': '3 4 3',
                '21KB1A0255': '3 4 3', '21KB1A0256': '3 4 3', '21KB1A0257': '3 4 3', '21KB1A0258': '3 4 3',
                '21KB1A0259': '3 4 3', '21KB1A0260': '3 4 3', '21KB1A0261': '3 4 3', '21KB1A0262': '3 4 3',
                '21KB1A0263': '3 4 3', '21KB1A0264': '3 4 3', '21KB1A0265': '3 4 3', '21KB1A0266': '3 4 3',
                '21KB1A0267': '3 4 3', '21KB1A0268': '3 4 3', '21KB1A0269': '3 4 3', '21KB1A0270': '3 4 3',
                '21KB1A0271': '3 4 3', '21KB1A0272': '3 4 3', '21KB1A0273': '3 4 3', '21KB1A0274': '3 4 3',
                '21KB1A0275': '3 4 3', '21KB1A0276': '3 4 3', '21KB1A0277': '3 4 3', '21KB1A0278': '3 4 3',
                '21KB1A0279': '3 4 3', '21KB1A0280': '3 4 3', '21KB1A0281': '3 4 3', '21KB1A0282': '3 4 3',
                '21KB1A0283': '3 4 3', '21KB1A0284': '3 4 3', '21KB1A0285': '3 4 3', '21KB1A0286': '3 4 3',
                '21KB1A0287': '3 4 3', '21KB1A0288': '3 4 3', '21KB1A0289': '3 4 3', '21KB1A0290': '3 4 3',
                '21KB1A0291': '3 4 3', '21KB1A0292': '3 4 3', '21KB1A0293': '3 4 3', '21KB1A0294': '3 4 3',
                '21KB1A0101': '3 6 1', '21KB1A0102': '3 6 1', '21KB1A0103': '3 6 1', '21KB1A0104': '3 6 1',
                '21KB1A0105': '3 6 1', '21KB1A0106': '3 6 1', '21KB1A0107': '3 6 1', '21KB1A0108': '3 6 1',
                '21KB1A0109': '3 6 1', '21KB1A0110': '3 6 1', '21KB1A0111': '3 6 1', '21KB1A0112': '3 6 1',
                '21KB1A0113': '3 6 1', '21KB1A0114': '3 6 1', '21KB1A0115': '3 6 1', '21KB1A0116': '3 6 1',
                '21KB1A0117': '3 6 1', '21KB1A0118': '3 6 1', '21KB1A0119': '3 6 1', '21KB1A0120': '3 6 1',
                '21KB1A0121': '3 6 1', '21KB1A0122': '3 6 1', '21KB1A0123': '3 6 1', '21KB1A0124': '3 6 1',
                '21KB1A0125': '3 6 1', '21KB1A0126': '3 6 1', '21KB1A0127': '3 6 1', '21KB1A0128': '3 6 1',
                '21KB1A0129': '3 6 1', '21KB1A0130': '3 6 1', '21KB1A0131': '3 6 1', '21KB1A0132': '3 6 1',
                '21KB1A0133': '3 6 1', '21KB1A0134': '3 6 1', '21KB1A0135': '3 6 1', '21KB1A0136': '3 6 1',
                '21KB1A0137': '3 6 1', '21KB1A0138': '3 6 1', '21KB1A1201': '3 10 1', '21KB1A1202': '3 10 1',
                '21KB1A1203': '3 10 1', '21KB1A1204': '3 10 1', '21KB1A1205': '3 10 1', '21KB1A1206': '3 10 1',
                '21KB1A1207': '3 10 1', '21KB1A1208': '3 10 1', '21KB1A1209': '3 10 1', '21KB1A1210': '3 10 1',
                '21KB1A1211': '3 10 1', '21KB1A1212': '3 10 1', '21KB1A1213': '3 10 1', '21KB1A1214': '3 10 1',
                '21KB1A1215': '3 10 1', '21KB1A1216': '3 10 1', '21KB1A1217': '3 10 1', '21KB1A1218': '3 10 1',
                '21KB1A1219': '3 10 1', '21KB1A1220': '3 10 1', '21KB1A1221': '3 10 1', '21KB1A1222': '3 10 1',
                '21KB1A1223': '3 10 1', '21KB1A1224': '3 10 1', '21KB1A1225': '3 10 1', '21KB1A1226': '3 10 1',
                '21KB1A1227': '3 10 1', '21KB1A1228': '3 10 1', '21KB1A1229': '3 10 1', '21KB1A1230': '3 10 1',
                '21KB1A1231': '3 10 1', '21KB1A1232': '3 10 1', '21KB1A1233': '3 10 1', '21KB1A1234': '3 10 1',
                '21KB1A1235': '3 10 1', '21KB1A1236': '3 10 1', '21KB1A1237': '3 10 1', '21KB1A1238': '3 10 1',
                '21KB1A1239': '3 10 1', '21KB1A1240': '3 10 1', '21KB1A1241': '3 10 1', '21KB1A1242': '3 10 1',
                '21KB1A1243': '3 10 1', '21KB1A1244': '3 10 1', '21KB1A1245': '3 10 1', '21KB1A1246': '3 10 1',
                '21KB1A1247': '3 10 1', '21KB1A1248': '3 10 1', '21KB1A3001': '3 11 2', '21KB1A3002': '3 11 2',
                '21KB1A3003': '3 11 2', '21KB1A3004': '3 11 2', '21KB1A3005': '3 11 2', '21KB1A3006': '3 11 2',
                '21KB1A3007': '3 11 2', '21KB1A3008': '3 11 2', '21KB1A3009': '3 11 2', '21KB1A3010': '3 11 2',
                '21KB1A3011': '3 11 2', '21KB1A3012': '3 11 2', '21KB1A3013': '3 11 2', '21KB1A3014': '3 11 2',
                '21KB1A3015': '3 11 2', '21KB1A3016': '3 11 2', '21KB1A3017': '3 11 2', '21KB1A3018': '3 11 2',
                '21KB1A3019': '3 11 2', '21KB1A3020': '3 11 2', '21KB1A3021': '3 11 2', '21KB1A3022': '3 11 2',
                '21KB1A3023': '3 11 2', '21KB1A3024': '3 11 2', '21KB1A3025': '3 11 2', '21KB1A3026': '3 11 2',
                '21KB1A3027': '3 11 2', '21KB1A3028': '3 11 2', '21KB1A3029': '3 11 2', '21KB1A3030': '3 11 2',
                '21KB1A3031': '3 11 2', '21KB1A3032': '3 11 2', '21KB1A3033': '3 11 2', '21KB1A3035': '3 11 2',
                '21KB1A3036': '3 11 2', '21KB1A3037': '3 11 2', '21KB1A3038': '3 11 2', '21KB1A3039': '3 11 2',
                '21KB1A3040': '3 11 2', '21KB1A3041': '3 11 2', '21KB1A3042': '3 11 2', '21KB1A3043': '3 11 2',
                '21KB1A3044': '3 11 2', '21KB1A3045': '3 11 2', '21KB1A3046': '3 11 2', '21KB1A3047': '3 11 2',
                '21KB1A3048': '3 11 2', '21KB1A3049': '3 11 2', '21KB1A3050': '3 11 2', '21KB1A3051': '3 11 2',
                '21KB1A3052': '3 11 2', '21KB1A3053': '3 11 3', '21KB1A3054': '3 11 3', '21KB1A3055': '3 11 3',
                '21KB1A3056': '3 11 3', '21KB1A3057': '3 11 3', '21KB1A3058': '3 11 3', '21KB1A3059': '3 11 3',
                '21KB1A3060': '3 11 3', '21KB1A3061': '3 11 3', '21KB1A3062': '3 11 3', '21KB1A3063': '3 11 3',
                '21KB1A3064': '3 11 3', '21KB1A3065': '3 11 3', '21KB1A3066': '3 11 3', '21KB1A3067': '3 11 3',
                '21KB1A3068': '3 11 3', '21KB1A3069': '3 11 3', '21KB1A3070': '3 11 3', '21KB1A3071': '3 11 3',
                '21KB1A3072': '3 11 3', '21KB1A3073': '3 11 3', '21KB1A3074': '3 11 3', '21KB1A3075': '3 11 3',
                '21KB1A3076': '3 11 3', '21KB1A3077': '3 11 3', '21KB1A3078': '3 11 3', '21KB1A3079': '3 11 3',
                '21KB1A3080': '3 11 3', '21KB1A3081': '3 11 3', '21KB1A3082': '3 11 3', '21KB1A3083': '3 11 3',
                '21KB1A3084': '3 11 3', '21KB1A3085': '3 11 3', '21KB1A3086': '3 11 3', '21KB1A3087': '3 11 3',
                '21KB1A3088': '3 11 3', '21KB1A3089': '3 11 3', '21KB1A3090': '3 11 3', '21KB1A3091': '3 11 3',
                '21KB1A3092': '3 11 3', '21KB1A3093': '3 11 3', '21KB1A3094': '3 11 3', '21KB1A3095': '3 11 3',
                '21KB1A3096': '3 11 3', '21KB1A3097': '3 11 3', '21KB1A3098': '3 11 3', '21KB1A3099': '3 11 3',
                '21KB1A30A0': '3 11 3', '21KB1A30A1': '3 11 3', '21KB1A30A2': '3 11 3', '21KB1A30A3': '3 11 3',
                '20KB1A0301': '5 1 2', '20KB1A0302': '5 1 2', '20KB1A0303': '5 1 2', '20KB1A0304': '5 1 2',
                '20KB1A0305': '5 1 2', '20KB1A0306': '5 1 2', '20KB1A0307': '5 1 2', '20KB1A0308': '5 1 2',
                '20KB1A0309': '5 1 2', '20KB1A0310': '5 1 2', '20KB1A0312': '5 1 2', '20KB1A0313': '5 1 2',
                '20KB1A0314': '5 1 2', '20KB1A0315': '5 1 2', '20KB1A0316': '5 1 2', '20KB1A0317': '5 1 2',
                '20KB1A0318': '5 1 2', '20KB1A0319': '5 1 2', '20KB1A0320': '5 1 2', '20KB1A0321': '5 1 2',
                '20KB1A0322': '5 1 2', '20KB1A0323': '5 1 2', '20KB1A0324': '5 1 2', '20KB1A0325': '5 1 2',
                '20KB1A0326': '5 1 2', '20KB1A0327': '5 1 2', '20KB1A0328': '5 1 2', '20KB1A0329': '5 1 2',
                '20KB1A0330': '5 1 2', '20KB1A0331': '5 1 2', '20KB1A0332': '5 1 2', '20KB1A0333': '5 1 2',
                '20KB1A0334': '5 1 2', '20KB1A0335': '5 1 2', '20KB1A0336': '5 1 2', '20KB1A0337': '5 1 2',
                '20KB1A0338': '5 1 2', '20KB1A0339': '5 1 2', '20KB1A0342': '5 1 2', '20KB1A0343': '5 1 2',
                '21KB5A0301': '5 1 2', '21KB5A0302': '5 1 2', '21KB5A0303': '5 1 2', '21KB5A0304': '5 1 2',
                '21KB5A0305': '5 1 2', '21KB5A0306': '5 1 2', '21KB5A0307': '5 1 2', '21KB5A0308': '5 1 2',
                '21KB5A0309': '5 1 2', '21KB5A0310': '5 1 2', '21KB5A0311': '5 1 2', '21KB5A0312': '5 1 2',
                '21KB5A0313': '5 1 2', '21KB5A0314': '5 1 2', '21KB5A0315': '5 1 2', '21KB5A0316': '5 1 2',
                '20KB1A0344': '5 1 3', '20KB1A0345': '5 1 3', '20KB1A0346': '5 1 3', '20KB1A0347': '5 1 3',
                '20KB1A0348': '5 1 3', '20KB1A0349': '5 1 3', '20KB1A0350': '5 1 3', '20KB1A0351': '5 1 3',
                '20KB1A0352': '5 1 3', '20KB1A0353': '5 1 3', '20KB1A0354': '5 1 3', '20KB1A0355': '5 1 3',
                '20KB1A0356': '5 1 3', '20KB1A0357': '5 1 3', '20KB1A0358': '5 1 3', '20KB1A0359': '5 1 3',
                '20KB1A0360': '5 1 3', '20KB1A0361': '5 1 3', '20KB1A0362': '5 1 3', '20KB1A0363': '5 1 3',
                '20KB1A0364': '5 1 3', '20KB1A0365': '5 1 3', '20KB1A0366': '5 1 3', '20KB1A0367': '5 1 3',
                '20KB1A0368': '5 1 3', '20KB1A0369': '5 1 3', '20KB1A0370': '5 1 3', '20KB1A0371': '5 1 3',
                '20KB1A0372': '5 1 3', '20KB1A0373': '5 1 3', '20KB1A0374': '5 1 3', '20KB1A0375': '5 1 3',
                '20KB1A0376': '5 1 3', '20KB1A0377': '5 1 3', '20KB1A0378': '5 1 3', '20KB1A0379': '5 1 3',
                '20KB1A0380': '5 1 3', '20KB1A0381': '5 1 3', '20KB1A0382': '5 1 3', '20KB1A0383': '5 1 3',
                '20KB1A0384': '5 1 3', '20KB1A0385': '5 1 3', '21KB5A0317': '5 1 3', '21KB5A0318': '5 1 3',
                '21KB5A0319': '5 1 3', '21KB5A0320': '5 1 3', '21KB5A0321': '5 1 3', '21KB5A0322': '5 1 3',
                '21KB5A0323': '5 1 3', '21KB5A0324': '5 1 3', '21KB5A0325': '5 1 3', '21KB5A0326': '5 1 3',
                '21KB5A0327': '5 1 3', '21KB5A0328': '5 1 3', '21KB5A0329': '5 1 3', '21KB5A0330': '5 1 3',
                '21KB5A0331': '5 1 3', '21KB5A0332': '5 1 3', '20KB1A0386': '5 1 4', '20KB1A0387': '5 1 4',
                '20KB1A0388': '5 1 4', '20KB1A0389': '5 1 4', '20KB1A0390': '5 1 4', '20KB1A0391': '5 1 4',
                '20KB1A0392': '5 1 4', '20KB1A0393': '5 1 4', '20KB1A0394': '5 1 4', '20KB1A0395': '5 1 4',
                '20KB1A0396': '5 1 4', '20KB1A0397': '5 1 4', '20KB1A0398': '5 1 4', '20KB1A0399': '5 1 4',
                '20KB1A03A0': '5 1 4', '20KB1A03A1': '5 1 4', '20KB1A03A2': '5 1 4', '20KB1A03A3': '5 1 4',
                '20KB1A03A4': '5 1 4', '20KB1A03A5': '5 1 4', '20KB1A03A6': '5 1 4', '20KB1A03A7': '5 1 4',
                '20KB1A03A8': '5 1 4', '20KB1A03A9': '5 1 4', '20KB1A03B0': '5 1 4', '20KB1A03B1': '5 1 4',
                '20KB1A03B2': '5 1 4', '20KB1A03B3': '5 1 4', '20KB1A03B4': '5 1 4', '20KB1A03B5': '5 1 4',
                '20KB1A03B6': '5 1 4', '20KB1A03B7': '5 1 4', '20KB1A03B8': '5 1 4', '20KB1A03B9': '5 1 4',
                '20KB1A03C0': '5 1 4', '20KB1A03C1': '5 1 4', '20KB1A03C2': '5 1 4', '20KB1A03C3': '5 1 4',
                '20KB1A03C4': '5 1 4', '20KB1A03C5': '5 1 4', '20KB1A03C6': '5 1 4', '20KB1A03C7': '5 1 4',
                '20KB1A03C8': '5 1 4', '21KB5A0333': '5 1 4', '21KB5A0334': '5 1 4', '21KB5A0335': '5 1 4',
                '21KB5A0336': '5 1 4', '21KB5A0337': '5 1 4', '21KB5A0338': '5 1 4', '21KB5A0339': '5 1 4',
                '21KB5A0340': '5 1 4', '21KB5A0341': '5 1 4', '21KB5A0342': '5 1 4', '21KB5A0343': '5 1 4',
                '21KB5A0344': '5 1 4', '21KB5A0345': '5 1 4', '21KB5A0346': '5 1 4', '21KB5A0347': '5 1 4',
                '21KB5A0348': '5 1 4', '20KB1A0501': '5 2 2', '20KB1A0502': '5 2 2', '20KB1A0503': '5 2 2',
                '20KB1A0504': '5 2 2', '20KB1A0505': '5 2 2', '20KB1A0506': '5 2 2', '20KB1A0507': '5 2 2',
                '20KB1A0508': '5 2 2', '20KB1A0509': '5 2 2', '20KB1A0510': '5 2 2', '20KB1A0511': '5 2 2',
                '20KB1A0512': '5 2 2', '20KB1A0513': '5 2 2', '20KB1A0514': '5 2 2', '20KB1A0515': '5 2 2',
                '20KB1A0516': '5 2 2', '20KB1A0517': '5 2 2', '20KB1A0518': '5 2 2', '20KB1A0519': '5 2 2',
                '20KB1A0520': '5 2 2', '20KB1A0521': '5 2 2', '20KB1A0522': '5 2 2', '20KB1A0523': '5 2 2',
                '20KB1A0524': '5 2 2', '20KB1A0525': '5 2 2', '20KB1A0526': '5 2 2', '20KB1A0527': '5 2 2',
                '20KB1A0528': '5 2 2', '20KB1A0529': '5 2 2', '20KB1A0530': '5 2 2', '20KB1A0531': '5 2 2',
                '20KB1A0532': '5 2 2', '20KB1A0533': '5 2 2', '20KB1A0534': '5 2 2', '20KB1A0535': '5 2 2',
                '20KB1A0536': '5 2 2', '20KB1A0537': '5 2 2', '20KB1A0538': '5 2 2', '20KB1A0539': '5 2 2',
                '20KB1A0540': '5 2 2', '20KB1A0541': '5 2 2', '20KB1A0542': '5 2 2', '20KB1A0543': '5 2 2',
                '20KB1A0544': '5 2 2', '20KB1A0545': '5 2 2', '20KB1A0546': '5 2 2', '20KB1A0547': '5 2 2',
                '20KB1A0548': '5 2 2', '20KB1A0549': '5 2 2', '20KB1A0550': '5 2 2', '20KB1A0551': '5 2 2',
                '20KB1A0552': '5 2 2', '20KB1A0553': '5 2 2', '20KB1A0554': '5 2 2', '20KB1A0555': '5 2 2',
                '20KB1A0556': '5 2 2', '20KB1A0557': '5 2 2', '20KB1A0558': '5 2 2', '20KB1A0559': '5 2 2',
                '20KB1A0560': '5 2 2', '20KB1A0561': '5 2 2', '20KB1A0562': '5 2 2', '20KB1A0563': '5 2 2',
                '20KB1A0564': '5 2 2', '21KB5A0501': '5 2 2', '21KB5A0502': '5 2 2', '21KB5A0503': '5 2 2',
                '21KB5A0504': '5 2 2', '21KB5A0505': '5 2 2', '21KB5A0506': '5 2 2', '20KB1A0565': '5 2 3',
                '20KB1A0566': '5 2 3', '20KB1A0567': '5 2 3', '20KB1A0568': '5 2 3', '20KB1A0569': '5 2 3',
                '20KB1A0570': '5 2 3', '20KB1A0571': '5 2 3', '20KB1A0572': '5 2 3', '20KB1A0573': '5 2 3',
                '20KB1A0574': '5 2 3', '20KB1A0576': '5 2 3', '20KB1A0577': '5 2 3', '20KB1A0578': '5 2 3',
                '20KB1A0579': '5 2 3', '20KB1A0580': '5 2 3', '20KB1A0581': '5 2 3', '20KB1A0582': '5 2 3',
                '20KB1A0583': '5 2 3', '20KB1A0584': '5 2 3', '20KB1A0585': '5 2 3', '20KB1A0586': '5 2 3',
                '20KB1A0587': '5 2 3', '20KB1A0588': '5 2 3', '20KB1A0589': '5 2 3', '20KB1A0590': '5 2 3',
                '20KB1A0591': '5 2 3', '20KB1A0592': '5 2 3', '20KB1A0593': '5 2 3', '20KB1A0594': '5 2 3',
                '20KB1A0595': '5 2 3', '20KB1A0596': '5 2 3', '20KB1A0597': '5 2 3', '20KB1A0599': '5 2 3',
                '20KB1A05A0': '5 2 3', '20KB1A05A1': '5 2 3', '20KB1A05A2': '5 2 3', '20KB1A05A3': '5 2 3',
                '20KB1A05A4': '5 2 3', '20KB1A05A5': '5 2 3', '20KB1A05A6': '5 2 3', '20KB1A05A7': '5 2 3',
                '20KB1A05A8': '5 2 3', '20KB1A05A9': '5 2 3', '20KB1A05B0': '5 2 3', '20KB1A05B1': '5 2 3',
                '20KB1A05B2': '5 2 3', '20KB1A05B3': '5 2 3', '20KB1A05B4': '5 2 3', '20KB1A05B5': '5 2 3',
                '20KB1A05B6': '5 2 3', '20KB1A05B7': '5 2 3', '20KB1A05B8': '5 2 3', '20KB1A05B9': '5 2 3',
                '20KB1A05C0': '5 2 3', '20KB1A05C1': '5 2 3', '20KB1A05C2': '5 2 3', '20KB1A05C3': '5 2 3',
                '20KB1A05C4': '5 2 3', '20KB1A05C5': '5 2 3', '20KB1A05C6': '5 2 3', '20KB1A05C7': '5 2 3',
                '20KB1A05C8': '5 2 3', '20KB1A05C9': '5 2 3', '21KB5A0507': '5 2 3', '21KB5A0508': '5 2 3',
                '21KB5A0509': '5 2 3', '21KB5A0510': '5 2 3', '21KB5A0511': '5 2 3', '21KB5A0512': '5 2 3',
                '20KB1A05D0': '5 2 4', '20KB1A05D1': '5 2 4', '20KB1A05D2': '5 2 4', '20KB1A05D3': '5 2 4',
                '20KB1A05D4': '5 2 4', '20KB1A05D5': '5 2 4', '20KB1A05D6': '5 2 4', '20KB1A05D7': '5 2 4',
                '20KB1A05D8': '5 2 4', '20KB1A05D9': '5 2 4', '20KB1A05E0': '5 2 4', '20KB1A05E1': '5 2 4',
                '20KB1A05E2': '5 2 4', '20KB1A05E3': '5 2 4', '20KB1A05E4': '5 2 4', '20KB1A05E5': '5 2 4',
                '20KB1A05E6': '5 2 4', '20KB1A05E7': '5 2 4', '20KB1A05E8': '5 2 4', '20KB1A05E9': '5 2 4',
                '20KB1A05F0': '5 2 4', '20KB1A05F1': '5 2 4', '20KB1A05F2': '5 2 4', '20KB1A05F3': '5 2 4',
                '20KB1A05F4': '5 2 4', '20KB1A05F5': '5 2 4', '20KB1A05F6': '5 2 4', '20KB1A05F7': '5 2 4',
                '20KB1A05F8': '5 2 4', '20KB1A05F9': '5 2 4', '20KB1A05G0': '5 2 4', '20KB1A05G1': '5 2 4',
                '20KB1A05G2': '5 2 4', '20KB1A05G3': '5 2 4', '20KB1A05G4': '5 2 4', '20KB1A05G5': '5 2 4',
                '20KB1A05G6': '5 2 4', '20KB1A05G7': '5 2 4', '20KB1A05G8': '5 2 4', '20KB1A05G9': '5 2 4',
                '20KB1A05H0': '5 2 4', '20KB1A05H1': '5 2 4', '20KB1A05H2': '5 2 4', '20KB1A05H3': '5 2 4',
                '20KB1A05H4': '5 2 4', '20KB1A05H5': '5 2 4', '20KB1A05H6': '5 2 4', '20KB1A05H7': '5 2 4',
                '20KB1A05H8': '5 2 4', '20KB1A05H9': '5 2 4', '20KB1A05I0': '5 2 4', '20KB1A05I1': '5 2 4',
                '20KB1A05I2': '5 2 4', '20KB1A05I3': '5 2 4', '20KB1A05I4': '5 2 4', '20KB1A05I5': '5 2 4',
                '20KB1A05I6': '5 2 4', '20KB1A05I7': '5 2 4', '20KB1A05I8': '5 2 4', '20KB1A05I9': '5 2 4',
                '20KB1A05J0': '5 2 4', '20KB1A05J1': '5 2 4', '20KB1A05J2': '5 2 4', '20KB1A05J3': '5 2 4',
                '18KB1A05E0': '5 2 4', '21KB5A0513': '5 2 4', '21KB5A0514': '5 2 4', '21KB5A0515': '5 2 4',
                '21KB5A0516': '5 2 4', '21KB5A0517': '5 2 4', '21KB5A0518': '5 2 4', '20KB1A0401': '5 3 2',
                '20KB1A0402': '5 3 2', '20KB1A0403': '5 3 2', '20KB1A0404': '5 3 2', '20KB1A0405': '5 3 2',
                '20KB1A0406': '5 3 2', '20KB1A0407': '5 3 2', '20KB1A0408': '5 3 2', '20KB1A0409': '5 3 2',
                '20KB1A0410': '5 3 2', '20KB1A0411': '5 3 2', '20KB1A0413': '5 3 2', '20KB1A0414': '5 3 2',
                '20KB1A0415': '5 3 2', '20KB1A0416': '5 3 2', '20KB1A0417': '5 3 2', '20KB1A0418': '5 3 2',
                '20KB1A0419': '5 3 2', '20KB1A0420': '5 3 2', '20KB1A0421': '5 3 2', '20KB1A0422': '5 3 2',
                '20KB1A0423': '5 3 2', '20KB1A0424': '5 3 2', '20KB1A0425': '5 3 2', '20KB1A0426': '5 3 2',
                '20KB1A0427': '5 3 2', '20KB1A0428': '5 3 2', '20KB1A0429': '5 3 2', '20KB1A0430': '5 3 2',
                '20KB1A0431': '5 3 2', '20KB1A0432': '5 3 2', '20KB1A0433': '5 3 2', '20KB1A0434': '5 3 2',
                '20KB1A0435': '5 3 2', '20KB1A0436': '5 3 2', '20KB1A0438': '5 3 2', '20KB1A0439': '5 3 2',
                '20KB1A0440': '5 3 2', '20KB1A0441': '5 3 2', '20KB1A0442': '5 3 2', '20KB1A0443': '5 3 2',
                '20KB1A0444': '5 3 2', '20KB1A0445': '5 3 2', '20KB1A0446': '5 3 2', '20KB1A0447': '5 3 2',
                '20KB1A0448': '5 3 2', '20KB1A0449': '5 3 2', '20KB1A0450': '5 3 2', '20KB1A0451': '5 3 2',
                '20KB1A0452': '5 3 2', '20KB1A0453': '5 3 2', '20KB1A0454': '5 3 2', '20KB1A0455': '5 3 2',
                '20KB1A0456': '5 3 2', '20KB1A0457': '5 3 2', '20KB1A0458': '5 3 2', '20KB1A0459': '5 3 2',
                '20KB1A0460': '5 3 2', '20KB1A0461': '5 3 2', '20KB1A0462': '5 3 2', '20KB1A0463': '5 3 2',
                '20KB1A0464': '5 3 2', '21KB5A0401': '5 3 2', '21KB5A0402': '5 3 2', '21KB5A0403': '5 3 2',
                '21KB5A0404': '5 3 2', '21KB5A0405': '5 3 2', '21KB5A0406': '5 3 2', '20KB1A0465': '5 3 3',
                '20KB1A0466': '5 3 3', '20KB1A0467': '5 3 3', '20KB1A0468': '5 3 3', '20KB1A0469': '5 3 3',
                '20KB1A0470': '5 3 3', '20KB1A0471': '5 3 3', '20KB1A0472': '5 3 3', '20KB1A0473': '5 3 3',
                '20KB1A0474': '5 3 3', '20KB1A0475': '5 3 3', '20KB1A0476': '5 3 3', '20KB1A0477': '5 3 3',
                '20KB1A0478': '5 3 3', '20KB1A0479': '5 3 3', '20KB1A0480': '5 3 3', '20KB1A0481': '5 3 3',
                '20KB1A0482': '5 3 3', '20KB1A0483': '5 3 3', '20KB1A0484': '5 3 3', '20KB1A0485': '5 3 3',
                '20KB1A0486': '5 3 3', '20KB1A0487': '5 3 3', '20KB1A0488': '5 3 3', '20KB1A0489': '5 3 3',
                '20KB1A0490': '5 3 3', '20KB1A0491': '5 3 3', '20KB1A0492': '5 3 3', '20KB1A0493': '5 3 3',
                '20KB1A0494': '5 3 3', '20KB1A0495': '5 3 3', '20KB1A0496': '5 3 3', '20KB1A0497': '5 3 3',
                '20KB1A0498': '5 3 3', '20KB1A04A0': '5 3 3', '20KB1A04A1': '5 3 3', '20KB1A04A2': '5 3 3',
                '20KB1A04A3': '5 3 3', '20KB1A04A4': '5 3 3', '20KB1A04A5': '5 3 3', '20KB1A04A6': '5 3 3',
                '20KB1A04A7': '5 3 3', '20KB1A04A8': '5 3 3', '20KB1A04A9': '5 3 3', '20KB1A04B0': '5 3 3',
                '20KB1A04B1': '5 3 3', '20KB1A04B2': '5 3 3', '20KB1A04B3': '5 3 3', '20KB1A04B4': '5 3 3',
                '20KB1A04B5': '5 3 3', '20KB1A04B6': '5 3 3', '20KB1A04B7': '5 3 3', '20KB1A04B8': '5 3 3',
                '20KB1A04B9': '5 3 3', '20KB1A04C0': '5 3 3', '20KB1A04C1': '5 3 3', '20KB1A04C2': '5 3 3',
                '20KB1A04C3': '5 3 3', '20KB1A04C4': '5 3 3', '20KB1A04C5': '5 3 3', '20KB1A04C6': '5 3 3',
                '20KB1A04C7': '5 3 3', '20KB1A04C8': '5 3 3', '21KB5A0407': '5 3 3', '21KB5A0408': '5 3 3',
                '21KB5A0409': '5 3 3', '21KB5A0410': '5 3 3', '21KB5A0411': '5 3 3', '21KB5A0412': '5 3 3',
                '20KB1A04C9': '5 3 4', '20KB1A04D0': '5 3 4', '20KB1A04D1': '5 3 4', '20KB1A04D2': '5 3 4',
                '20KB1A04D3': '5 3 4', '20KB1A04D4': '5 3 4', '20KB1A04D5': '5 3 4', '20KB1A04D6': '5 3 4',
                '20KB1A04D7': '5 3 4', '20KB1A04D8': '5 3 4', '20KB1A04D9': '5 3 4', '20KB1A04E0': '5 3 4',
                '20KB1A04E1': '5 3 4', '20KB1A04E2': '5 3 4', '20KB1A04E3': '5 3 4', '20KB1A04E4': '5 3 4',
                '20KB1A04E5': '5 3 4', '20KB1A04E6': '5 3 4', '20KB1A04E7': '5 3 4', '20KB1A04E8': '5 3 4',
                '20KB1A04E9': '5 3 4', '20KB1A04F0': '5 3 4', '20KB1A04F1': '5 3 4', '20KB1A04F2': '5 3 4',
                '20KB1A04F3': '5 3 4', '20KB1A04F4': '5 3 4', '20KB1A04F5': '5 3 4', '20KB1A04F6': '5 3 4',
                '20KB1A04F7': '5 3 4', '20KB1A04F8': '5 3 4', '20KB1A04F9': '5 3 4', '20KB1A04G0': '5 3 4',
                '20KB1A04G1': '5 3 4', '20KB1A04G2': '5 3 4', '20KB1A04G3': '5 3 4', '20KB1A04G4': '5 3 4',
                '20KB1A04G5': '5 3 4', '20KB1A04G6': '5 3 4', '20KB1A04G7': '5 3 4', '20KB1A04G8': '5 3 4',
                '20KB1A04G9': '5 3 4', '20KB1A04H0': '5 3 4', '20KB1A04H1': '5 3 4', '20KB1A04H2': '5 3 4',
                '20KB1A04H3': '5 3 4', '20KB1A04H4': '5 3 4', '20KB1A04H5': '5 3 4', '20KB1A04H6': '5 3 4',
                '20KB1A04H7': '5 3 4', '20KB1A04H8': '5 3 4', '20KB1A04H9': '5 3 4', '20KB1A04I0': '5 3 4',
                '20KB1A04I1': '5 3 4', '20KB1A04I2': '5 3 4', '20KB1A04I3': '5 3 4', '20KB1A04I4': '5 3 4',
                '20KB1A04I5': '5 3 4', '20KB1A04I6': '5 3 4', '20KB1A04I7': '5 3 4', '20KB1A04I8': '5 3 4',
                '20KB1A04I9': '5 3 4', '20KB1A04J0': '5 3 4', '20KB1A04J1': '5 3 4', '21KB5A0413': '5 3 4',
                '21KB5A0414': '5 3 4', '21KB5A0415': '5 3 4', '21KB5A0416': '5 3 4', '21KB5A0417': '5 3 4',
                '21KB5A0418': '5 3 4', '21KB5A0419': '5 3 4', '20KB1A0201': '5 4 2', '20KB1A0202': '5 4 2',
                '20KB1A0203': '5 4 2', '20KB1A0204': '5 4 2', '20KB1A0205': '5 4 2', '20KB1A0206': '5 4 2',
                '20KB1A0207': '5 4 2', '20KB1A0208': '5 4 2', '20KB1A0209': '5 4 2', '20KB1A0210': '5 4 2',
                '20KB1A0211': '5 4 2', '20KB1A0212': '5 4 2', '20KB1A0213': '5 4 2', '20KB1A0214': '5 4 2',
                '20KB1A0215': '5 4 2', '20KB1A0216': '5 4 2', '20KB1A0217': '5 4 2', '20KB1A0218': '5 4 2',
                '20KB1A0219': '5 4 2', '20KB1A0220': '5 4 2', '20KB1A0221': '5 4 2', '20KB1A0222': '5 4 2',
                '20KB1A0223': '5 4 2', '20KB1A0224': '5 4 2', '20KB1A0225': '5 4 2', '20KB1A0226': '5 4 2',
                '20KB1A0227': '5 4 2', '20KB1A0228': '5 4 2', '20KB1A0229': '5 4 2', '20KB1A0230': '5 4 2',
                '20KB1A0231': '5 4 2', '20KB1A0232': '5 4 2', '20KB1A0233': '5 4 2', '20KB1A0234': '5 4 2',
                '20KB1A0235': '5 4 2', '20KB1A0236': '5 4 2', '20KB1A0237': '5 4 2', '20KB1A0238': '5 4 2',
                '20KB1A0239': '5 4 2', '20KB1A0240': '5 4 2', '20KB1A0241': '5 4 2', '20KB1A0242': '5 4 2',
                '20KB1A0243': '5 4 2', '20KB1A0244': '5 4 2', '20KB1A0245': '5 4 2', '21KB5A0201': '5 4 2',
                '21KB5A0202': '5 4 2', '21KB5A0203': '5 4 2', '21KB5A0204': '5 4 2', '21KB5A0205': '5 4 2',
                '21KB5A0206': '5 4 2', '21KB5A0207': '5 4 2', '21KB5A0208': '5 4 2', '21KB5A0209': '5 4 2',
                '21KB5A0210': '5 4 2', '21KB5A0211': '5 4 2', '20KB1A0246': '5 4 3', '20KB1A0247': '5 4 3',
                '20KB1A0248': '5 4 3', '20KB1A0250': '5 4 3', '20KB1A0251': '5 4 3', '20KB1A0252': '5 4 3',
                '20KB1A0253': '5 4 3', '20KB1A0254': '5 4 3', '20KB1A0255': '5 4 3', '20KB1A0256': '5 4 3',
                '20KB1A0257': '5 4 3', '20KB1A0258': '5 4 3', '20KB1A0259': '5 4 3', '20KB1A0260': '5 4 3',
                '20KB1A0261': '5 4 3', '20KB1A0263': '5 4 3', '20KB1A0264': '5 4 3', '20KB1A0265': '5 4 3',
                '20KB1A0266': '5 4 3', '20KB1A0267': '5 4 3', '20KB1A0268': '5 4 3', '20KB1A0269': '5 4 3',
                '20KB1A0270': '5 4 3', '20KB1A0271': '5 4 3', '20KB1A0272': '5 4 3', '20KB1A0273': '5 4 3',
                '20KB1A0274': '5 4 3', '20KB1A0275': '5 4 3', '20KB1A0276': '5 4 3', '20KB1A0277': '5 4 3',
                '20KB1A0278': '5 4 3', '20KB1A0279': '5 4 3', '20KB1A0280': '5 4 3', '20KB1A0281': '5 4 3',
                '20KB1A0282': '5 4 3', '20KB1A0283': '5 4 3', '20KB1A0284': '5 4 3', '20KB1A0285': '5 4 3',
                '20KB1A0286': '5 4 3', '20KB1A0287': '5 4 3', '20KB1A0288': '5 4 3', '20KB1A0289': '5 4 3',
                '20KB1A0290': '5 4 3', '21KB5A0212': '5 4 3', '21KB5A0213': '5 4 3', '21KB5A0214': '5 4 3',
                '21KB5A0215': '5 4 3', '21KB5A0216': '5 4 3', '21KB5A0217': '5 4 3', '21KB5A0218': '5 4 3',
                '21KB5A0219': '5 4 3', '21KB5A0220': '5 4 3', '21KB5A0221': '5 4 3', '21KB5A0222': '5 4 3',
                '19KB1A0244': '5 4 3', '': '5 11 4', '20KB1A0101': '5 6 2', '20KB1A0102': '5 6 2',
                '20KB1A0103': '5 6 2', '20KB1A0104': '5 6 2', '20KB1A0105': '5 6 2', '20KB1A0106': '5 6 2',
                '20KB1A0107': '5 6 2', '20KB1A0108': '5 6 2', '20KB1A0109': '5 6 2', '20KB1A0110': '5 6 2',
                '20KB1A0111': '5 6 2', '20KB1A0112': '5 6 2', '20KB1A0113': '5 6 2', '20KB1A0114': '5 6 2',
                '20KB1A0115': '5 6 2', '20KB1A0116': '5 6 2', '20KB1A0117': '5 6 2', '20KB1A0118': '5 6 2',
                '20KB1A0119': '5 6 2', '20KB1A0120': '5 6 2', '20KB1A0121': '5 6 2', '20KB1A0122': '5 6 2',
                '20KB1A0123': '5 6 2', '20KB1A0124': '5 6 2', '20KB1A0125': '5 6 2', '20KB1A0126': '5 6 2',
                '20KB1A0127': '5 6 2', '20KB1A0128': '5 6 2', '20KB1A0129': '5 6 2', '20KB1A0130': '5 6 2',
                '20KB1A0131': '5 6 2', '20KB1A0132': '5 6 2', '20KB1A0133': '5 6 2', '20KB1A0135': '5 6 2',
                '20KB1A0136': '5 6 2', '20KB1A0137': '5 6 2', '20KB1A0138': '5 6 2', '20KB1A0139': '5 6 2',
                '20KB1A0140': '5 6 2', '21KB5A0101': '5 6 2', '21KB5A0102': '5 6 2', '21KB5A0103': '5 6 2',
                '21KB5A0104': '5 6 2', '21KB5A0105': '5 6 2', '21KB5A0106': '5 6 2', '21KB5A0107': '5 6 2',
                '21KB5A0108': '5 6 2', '21KB5A0109': '5 6 2', '21KB5A0110': '5 6 2', '21KB5A0111': '5 6 2',
                '21KB5A0112': '5 6 2', '21KB5A0113': '5 6 2', '21KB5A0114': '5 6 2', '20KB1A0141': '5 6 3',
                '20KB1A0142': '5 6 3', '20KB1A0143': '5 6 3', '20KB1A0144': '5 6 3', '20KB1A0145': '5 6 3',
                '20KB1A0146': '5 6 3', '20KB1A0147': '5 6 3', '20KB1A0148': '5 6 3', '20KB1A0149': '5 6 3',
                '20KB1A0150': '5 6 3', '20KB1A0151': '5 6 3', '20KB1A0152': '5 6 3', '20KB1A0153': '5 6 3',
                '20KB1A0154': '5 6 3', '20KB1A0155': '5 6 3', '20KB1A0156': '5 6 3', '20KB1A0157': '5 6 3',
                '20KB1A0158': '5 6 3', '20KB1A0159': '5 6 3', '20KB1A0160': '5 6 3', '20KB1A0161': '5 6 3',
                '20KB1A0162': '5 6 3', '20KB1A0163': '5 6 3', '20KB1A0164': '5 6 3', '20KB1A0165': '5 6 3',
                '20KB1A0166': '5 6 3', '20KB1A0167': '5 6 3', '20KB1A0168': '5 6 3', '20KB1A0169': '5 6 3',
                '20KB1A0170': '5 6 3', '20KB1A0171': '5 6 3', '20KB1A0172': '5 6 3', '20KB1A0173': '5 6 3',
                '20KB1A0174': '5 6 3', '20KB1A0175': '5 6 3', '20KB1A0176': '5 6 3', '20KB1A0177': '5 6 3',
                '20KB1A0178': '5 6 3', '20KB1A0179': '5 6 3', '21KB5A0115': '5 6 3', '21KB5A0116': '5 6 3',
                '21KB5A0117': '5 6 3', '21KB5A0118': '5 6 3', '21KB5A0119': '5 6 3', '21KB5A0120': '5 6 3',
                '21KB5A0121': '5 6 3', '21KB5A0122': '5 6 3', '21KB5A0123': '5 6 3', '21KB5A0124': '5 6 3',
                '21KB5A0125': '5 6 3', '21KB5A0126': '5 6 3', '21KB5A0127': '5 6 3', '21KB5A0128': '5 6 3',
                '21KB5A0129': '5 6 3', '21KB5A0130': '5 6 3', '20KB1A1201': '5 10 1', '20KB1A1202': '5 10 1',
                '20KB1A1203': '5 10 1', '20KB1A1204': '5 10 1', '20KB1A1205': '5 10 1', '20KB1A1206': '5 10 1',
                '20KB1A1207': '5 10 1', '20KB1A1208': '5 10 1', '20KB1A1209': '5 10 1', '20KB1A1210': '5 10 1',
                '20KB1A1211': '5 10 1', '20KB1A1212': '5 10 1', '20KB1A1213': '5 10 1', '20KB1A1214': '5 10 1',
                '20KB1A1215': '5 10 1', '20KB1A1216': '5 10 1', '20KB1A1217': '5 10 1', '20KB1A1218': '5 10 1',
                '20KB1A1219': '5 10 1', '20KB1A1220': '5 10 1', '20KB1A1221': '5 10 1', '20KB1A1222': '5 10 1',
                '20KB1A1224': '5 10 1', '20KB1A1225': '5 10 1', '20KB1A1226': '5 10 1', '20KB1A1227': '5 10 1',
                '20KB1A1228': '5 10 1', '20KB1A1229': '5 10 1', '20KB1A1230': '5 10 1', '20KB1A1231': '5 10 1',
                '20KB1A1232': '5 10 1', '20KB1A1233': '5 10 1', '20KB1A1234': '5 10 1', '20KB1A1235': '5 10 1',
                '20KB1A1236': '5 10 1', '20KB1A1237': '5 10 1', '20KB1A1238': '5 10 1', '20KB1A1239': '5 10 1',
                '20KB1A1240': '5 10 1', '20KB1A1241': '5 10 1', '20KB1A1242': '5 10 1', '20KB1A1243': '5 10 1',
                '20KB1A1244': '5 10 1', '20KB1A1245': '5 10 1', '20KB1A1246': '5 10 1', '20KB1A1247': '5 10 1',
                '20KB1A1248': '5 10 1', '20KB1A1249': '5 10 1', '20KB1A1250': '5 10 1', '20KB1A1251': '5 10 1',
                '20KB1A1252': '5 10 1', '20KB1A1253': '5 10 1', '20KB1A1254': '5 10 1', '20KB1A1255': '5 10 1',
                '20KB1A1256': '5 10 1', '20KB1A1257': '5 10 1', '20KB1A1258': '5 10 1', '20KB1A1259': '5 10 1',
                '20KB1A1260': '5 10 1', '20KB1A1261': '5 10 1', '20KB1A1262': '5 10 1', '21KB5A1201': '5 10 1',
                '21KB5A1202': '5 10 1', '21KB5A1203': '5 10 1', '21KB5A1204': '5 10 1', '21KB5A1205': '5 10 1',
                '21KB5A1206': '5 10 1', '20KB1A3001': '5 11 1', '20KB1A3002': '5 11 1', '20KB1A3003': '5 11 1',
                '20KB1A3004': '5 11 1', '20KB1A3005': '5 11 1', '20KB1A3007': '5 11 1', '20KB1A3008': '5 11 1',
                '20KB1A3009': '5 11 1', '20KB1A3010': '5 11 1', '20KB1A3011': '5 11 1', '20KB1A3012': '5 11 1',
                '20KB1A3013': '5 11 1', '20KB1A3014': '5 11 1', '20KB1A3015': '5 11 1', '20KB1A3016': '5 11 1',
                '20KB1A3017': '5 11 1', '20KB1A3018': '5 11 1', '20KB1A3019': '5 11 1', '20KB1A3020': '5 11 1',
                '20KB1A3021': '5 11 1', '20KB1A3022': '5 11 1', '20KB1A3023': '5 11 1', '20KB1A3024': '5 11 1',
                '20KB1A3025': '5 11 1', '20KB1A3026': '5 11 1', '20KB1A3027': '5 11 1', '20KB1A3028': '5 11 1',
                '20KB1A3029': '5 11 1', '20KB1A3030': '5 11 1', '20KB1A3031': '5 11 1', '20KB1A3032': '5 11 1',
                '20KB1A3033': '5 11 1', '20KB1A3034': '5 11 1', '20KB1A3035': '5 11 1', '20KB1A3036': '5 11 1',
                '20KB1A3037': '5 11 1', '20KB1A3038': '5 11 1', '20KB1A3039': '5 11 1', '20KB1A3040': '5 11 1',
                '20KB1A3041': '5 11 1', '20KB1A3042': '5 11 1', '20KB1A3043': '5 11 1', '20KB1A3044': '5 11 1',
                '20KB1A3045': '5 11 1', '20KB1A3046': '5 11 1', '20KB1A3047': '5 11 1', '20KB1A3048': '5 11 1',
                '20KB1A3049': '5 11 1', '20KB1A3050': '5 11 1', '20KB1A3051': '5 11 1', '20KB1A3052': '5 11 1',
                '20KB1A3053': '5 11 1', '20KB1A3054': '5 11 1', '20KB1A3055': '5 11 1', '20KB1A3056': '5 11 1',
                '20KB1A3057': '5 11 1', '20KB1A3058': '5 11 1', '20KB1A3059': '5 11 1', '20KB1A3060': '5 11 1',
                '20KB1A3061': '5 11 1', '20KB1A3062': '5 11 1', '20KB1A3063': '5 11 1', '20KB1A3064': '5 11 1',
                '21KB5A3001': '5 11 1', '21KB5A3002': '5 11 1', '21KB5A3003': '5 11 1', '21KB5A3004': '5 11 1',
                '21KB5A3005': '5 11 1', '21KB5A3006': '5 11 1', '19KB1A1201': '6 10 1', '19KB1A1202': '6 10 1',
                '19KB1A1203': '6 10 1', '19KB1A1204': '6 10 1', '19KB1A1205': '6 10 1', '19KB1A1206': '6 10 1',
                '19KB1A1208': '6 10 1', '19KB1A1209': '6 10 1', '19KB1A1210': '6 10 1', '19KB1A1211': '6 10 1',
                '19KB1A1212': '6 10 1', '19KB1A1213': '6 10 1', '19KB1A1214': '6 10 1', '19KB1A1215': '6 10 1',
                '19KB1A1216': '6 10 1', '19KB1A1218': '6 10 1', '19KB1A1219': '6 10 1', '19KB1A1220': '6 10 1',
                '19KB1A1221': '6 10 1', '19KB1A1222': '6 10 1', '19KB1A1223': '6 10 1', '19KB1A1224': '6 10 1',
                '19KB1A1225': '6 10 1', '19KB1A1226': '6 10 1', '19KB1A1227': '6 10 1', '19KB1A1228': '6 10 1',
                '19KB1A1229': '6 10 1', '19KB1A1230': '6 10 1', '19KB1A1231': '6 10 1', '19KB1A1232': '6 10 1',
                '19KB1A1233': '6 10 1', '19KB1A1234': '6 10 1', '19KB1A1235': '6 10 1', '19KB1A1236': '6 10 1',
                '19KB1A1237': '6 10 1', '19KB1A1239': '6 10 1', '19KB1A1240': '6 10 1', '19KB1A1241': '6 10 1',
                '19KB1A1242': '6 10 1', '19KB1A1243': '6 10 1', '19KB1A1244': '6 10 1', '19KB1A1245': '6 10 1',
                '19KB1A1246': '6 10 1', '19KB1A1247': '6 10 1', '19KB1A1248': '6 10 1', '19KB1A1250': '6 10 1',
                '19KB1A1251': '6 10 1', '19KB1A1252': '6 10 1', '19KB1A1253': '6 10 1', '19KB1A1254': '6 10 1',
                '19KB1A1255': '6 10 1', '19KB1A0301': '6 1 2', '19KB1A0302': '6 1 2', '19KB1A0303': '6 1 2',
                '19KB1A0304': '6 1 2', '19KB1A0305': '6 1 2', '19KB1A0306': '6 1 2', '19KB1A0307': '6 1 2',
                '19KB1A0308': '6 1 2', '19KB1A0309': '6 1 2', '19KB1A0310': '6 1 2', '19KB1A0311': '6 1 2',
                '19KB1A0312': '6 1 2', '19KB1A0313': '6 1 2', '19KB1A0314': '6 1 2', '19KB1A0315': '6 1 2',
                '19KB1A0316': '6 1 2', '19KB1A0317': '6 1 2', '19KB1A0318': '6 1 2', '19KB1A0319': '6 1 2',
                '19KB1A0320': '6 1 2', '19KB1A0322': '6 1 2', '19KB1A0323': '6 1 2', '19KB1A0324': '6 1 2',
                '19KB1A0325': '6 1 2', '19KB1A0326': '6 1 2', '19KB1A0327': '6 1 2', '19KB1A0328': '6 1 2',
                '19KB1A0329': '6 1 2', '19KB1A0330': '6 1 2', '19KB1A0331': '6 1 2', '19KB1A0332': '6 1 2',
                '19KB1A0333': '6 1 2', '19KB1A0334': '6 1 2', '19KB1A0335': '6 1 2', '19KB1A0336': '6 1 2',
                '19KB1A0337': '6 1 2', '19KB1A0338': '6 1 2', '19KB1A0339': '6 1 2', '19KB1A0340': '6 1 2',
                '19KB1A0341': '6 1 2', '19KB1A0342': '6 1 2', '19KB1A0343': '6 1 2', '19KB1A0344': '6 1 2',
                '19KB1A0345': '6 1 2', '19KB1A0347': '6 1 2', '19KB1A0348': '6 1 2', '19KB1A0349': '6 1 2',
                '19KB1A0350': '6 1 2', '19KB1A0351': '6 1 2', '19KB1A0501': '6 2 2', '19KB1A0502': '6 2 2',
                '19KB1A0503': '6 2 2', '19KB1A0505': '6 2 2', '19KB1A0506': '6 2 2', '19KB1A0507': '6 2 2',
                '19KB1A0508': '6 2 2', '19KB1A0509': '6 2 2', '19KB1A0510': '6 2 2', '19KB1A0511': '6 2 2',
                '19KB1A0512': '6 2 2', '19KB1A0513': '6 2 2', '19KB1A0514': '6 2 2', '19KB1A0515': '6 2 2',
                '19KB1A0516': '6 2 2', '19KB1A0517': '6 2 2', '19KB1A0518': '6 2 2', '19KB1A0519': '6 2 2',
                '19KB1A0520': '6 2 2', '19KB1A0521': '6 2 2', '19KB1A0522': '6 2 2', '19KB1A0523': '6 2 2',
                '19KB1A0524': '6 2 2', '19KB1A0525': '6 2 2', '19KB1A0526': '6 2 2', '19KB1A0527': '6 2 2',
                '19KB1A0528': '6 2 2', '19KB1A0529': '6 2 2', '19KB1A0530': '6 2 2', '19KB1A0531': '6 2 2',
                '19KB1A0532': '6 2 2', '19KB1A0533': '6 2 2', '19KB1A0534': '6 2 2', '19KB1A0535': '6 2 2',
                '19KB1A0536': '6 2 2', '19KB1A0537': '6 2 2', '19KB1A0538': '6 2 2', '19KB1A0539': '6 2 2',
                '19KB1A0540': '6 2 2', '19KB1A0541': '6 2 2', '19KB1A0542': '6 2 2', '19KB1A0543': '6 2 2',
                '19KB1A0544': '6 2 2', '19KB1A0545': '6 2 2', '19KB1A0546': '6 2 2', '19KB1A0547': '6 2 2',
                '19KB1A0548': '6 2 2', '19KB1A0549': '6 2 2', '19KB1A0550': '6 2 2', '19KB1A0551': '6 2 2',
                '19KB1A0552': '6 2 2', '19KB1A0553': '6 2 2', '19KB1A0554': '6 2 2', '19KB1A0555': '6 2 2',
                '19KB1A0556': '6 2 2', '19KB1A0557': '6 2 2', '19KB1A0558': '6 2 2', '19KB1A0559': '6 2 2',
                '19KB1A0560': '6 2 2', '19KB1A0561': '6 2 2', '19KB1A0562': '6 2 2', '19KB1A0563': '6 2 2',
                '19KB1A0564': '6 2 2', '20KB5A0501': '6 2 2', '20KB5A0502': '6 2 2', '20KB5A0503': '6 2 2',
                '20KB5A0504': '6 2 2', '20KB5A0505': '6 2 2', '20KB5A0506': '6 2 2', '16KB1A0553': '6 2 2',
                '19KB1A0401': '6 3 2', '19KB1A0402': '6 3 2', '19KB1A0403': '6 3 2', '19KB1A0404': '6 3 2',
                '19KB1A0405': '6 3 2', '19KB1A0406': '6 3 2', '19KB1A0407': '6 3 2', '19KB1A0408': '6 3 2',
                '19KB1A0409': '6 3 2', '19KB1A0410': '6 3 2', '19KB1A0411': '6 3 2', '19KB1A0412': '6 3 2',
                '19KB1A0413': '6 3 2', '19KB1A0414': '6 3 2', '19KB1A0415': '6 3 2', '19KB1A0416': '6 3 2',
                '19KB1A0417': '6 3 2', '19KB1A0418': '6 3 2', '19KB1A0419': '6 3 2', '19KB1A0420': '6 3 2',
                '19KB1A0421': '6 3 2', '19KB1A0422': '6 3 2', '19KB1A0423': '6 3 2', '19KB1A0424': '6 3 2',
                '19KB1A0425': '6 3 2', '19KB1A0426': '6 3 2', '19KB1A0427': '6 3 2', '19KB1A0428': '6 3 2',
                '19KB1A0429': '6 3 2', '19KB1A0430': '6 3 2', '19KB1A0431': '6 3 2', '19KB1A0432': '6 3 2',
                '19KB1A0433': '6 3 2', '19KB1A0434': '6 3 2', '19KB1A0435': '6 3 2', '19KB1A0436': '6 3 2',
                '19KB1A0437': '6 3 2', '19KB1A0438': '6 3 2', '19KB1A0439': '6 3 2', '19KB1A0440': '6 3 2',
                '19KB1A0441': '6 3 2', '19KB1A0442': '6 3 2', '19KB1A0443': '6 3 2', '19KB1A0444': '6 3 2',
                '19KB1A0445': '6 3 2', '19KB1A0446': '6 3 2', '19KB1A0447': '6 3 2', '19KB1A0448': '6 3 2',
                '19KB1A0449': '6 3 2', '19KB1A0450': '6 3 2', '19KB1A0451': '6 3 2', '19KB1A0452': '6 3 2',
                '19KB1A0453': '6 3 2', '19KB1A0454': '6 3 2', '19KB1A0455': '6 3 2', '19KB1A0456': '6 3 2',
                '19KB1A0457': '6 3 2', '19KB1A0458': '6 3 2', '19KB1A0459': '6 3 2', '19KB1A0460': '6 3 2',
                '19KB1A0461': '6 3 2', '19KB1A0462': '6 3 2', '19KB1A0463': '6 3 2', '19KB1A0464': '6 3 2',
                '19KB1A0201': '6 4 2', '19KB1A0202': '6 4 2', '19KB1A0203': '6 4 2', '19KB1A0204': '6 4 2',
                '19KB1A0205': '6 4 2', '19KB1A0206': '6 4 2', '19KB1A0207': '6 4 2', '19KB1A0208': '6 4 2',
                '19KB1A0209': '6 4 2', '19KB1A0210': '6 4 2', '19KB1A0211': '6 4 2', '19KB1A0212': '6 4 2',
                '19KB1A0213': '6 4 2', '19KB1A0214': '6 4 2', '19KB1A0215': '6 4 2', '19KB1A0216': '6 4 2',
                '19KB1A0217': '6 4 2', '19KB1A0218': '6 4 2', '19KB1A0219': '6 4 2', '19KB1A0220': '6 4 2',
                '19KB1A0221': '6 4 2', '19KB1A0222': '6 4 2', '19KB1A0223': '6 4 2', '19KB1A0224': '6 4 2',
                '19KB1A0225': '6 4 2', '19KB1A0226': '6 4 2', '19KB1A0227': '6 4 2', '19KB1A0228': '6 4 2',
                '19KB1A0229': '6 4 2', '19KB1A0230': '6 4 2', '19KB1A0231': '6 4 2', '19KB1A0232': '6 4 2',
                '19KB1A0233': '6 4 2', '19KB1A0234': '6 4 2', '19KB1A0235': '6 4 2', '19KB1A0236': '6 4 2',
                '19KB1A0237': '6 4 2', '19KB1A0238': '6 4 2', '19KB1A0239': '6 4 2', '20KB5A0201': '6 4 2',
                '20KB5A0202': '6 4 2', '20KB5A0203': '6 4 2', '20KB5A0204': '6 4 2', '20KB5A0205': '6 4 2',
                '20KB5A0206': '6 4 2', '20KB5A0207': '6 4 2', '20KB5A0208': '6 4 2', '20KB5A0209': '6 4 2',
                '20KB5A0210': '6 4 2', '20KB5A0211': '6 4 2', '20KB5A0212': '6 4 2', '20KB5A0213': '6 4 2',
                '20KB5A0214': '6 4 2', '20KB5A0215': '6 4 2', '20KB5A0216': '6 4 2', '20KB5A0217': '6 4 2',
                '20KB5A0218': '6 4 2', '20KB5A0219': '6 4 2', '20KB5A0220': '6 4 2', '20KB5A0221': '6 4 2',
                '19KB1A0101': '6 6 2', '19KB1A0103': '6 6 2', '19KB1A0104': '6 6 2', '19KB1A0105': '6 6 2',
                '19KB1A0106': '6 6 2', '19KB1A0107': '6 6 2', '19KB1A0108': '6 6 2', '19KB1A0109': '6 6 2',
                '19KB1A0110': '6 6 2', '19KB1A0111': '6 6 2', '19KB1A0112': '6 6 2', '19KB1A0113': '6 6 2',
                '19KB1A0114': '6 6 2', '19KB1A0115': '6 6 2', '19KB1A0116': '6 6 2', '19KB1A0117': '6 6 2',
                '19KB1A0118': '6 6 2', '19KB1A0119': '6 6 2', '19KB1A0120': '6 6 2', '19KB1A0121': '6 6 2',
                '19KB1A0122': '6 6 2', '19KB1A0123': '6 6 2', '19KB1A0124': '6 6 2', '19KB1A0125': '6 6 2',
                '19KB1A0126': '6 6 2', '19KB1A0127': '6 6 2', '19KB1A0128': '6 6 2', '19KB1A0129': '6 6 2',
                '19KB1A0130': '6 6 2', '19KB1A0131': '6 6 2', '19KB1A0132': '6 6 2', '19KB1A0133': '6 6 2',
                '19KB1A0134': '6 6 2', '19KB1A0135': '6 6 2', '19KB1A0136': '6 6 2', '19KB1A0137': '6 6 2',
                '19KB1A0138': '6 6 2', '19KB1A0139': '6 6 2', '19KB1A0141': '6 6 2', '19KB1A0142': '6 6 2',
                '19KB1A0143': '6 6 2', '19KB1A0144': '6 6 2', '19KB1A0145': '6 6 2', '19KB1A0146': '6 6 2',
                '19KB1A0147': '6 6 2', '19KB1A0148': '6 6 2', '19KB1A0149': '6 6 2', '19KB1A0150': '6 6 2',
                '19KB1A0151': '6 6 2', '19KB1A0153': '6 6 2', '19KB1A0154': '6 6 2', '19KB1A0155': '6 6 2',
                '19KB1A0156': '6 6 2', '19KB1A0157': '6 6 2', '19KB1A0158': '6 6 2', '19KB1A0159': '6 6 2',
                '19KB1A0160': '6 6 2', '19KB1A0161': '6 6 2', '19KB1A0162': '6 6 2', '19KB1A0163': '6 6 2',
                '19KB1A0164': '6 6 2', '19KB1A0165': '6 6 2', '19KB1A0166': '6 6 2', '19KB1A0167': '6 6 2',
                '19KB1A0168': '6 6 2', '18KB1A0140': '6 6 2', '19KB1A0352': '6 1 3', '19KB1A0353': '6 1 3',
                '19KB1A0354': '6 1 3', '19KB1A0355': '6 1 3', '19KB1A0356': '6 1 3', '19KB1A0357': '6 1 3',
                '19KB1A0358': '6 1 3', '19KB1A0359': '6 1 3', '19KB1A0361': '6 1 3', '19KB1A0362': '6 1 3',
                '19KB1A0363': '6 1 3', '19KB1A0364': '6 1 3', '19KB1A0365': '6 1 3', '19KB1A0366': '6 1 3',
                '19KB1A0367': '6 1 3', '19KB1A0368': '6 1 3', '19KB1A0369': '6 1 3', '19KB1A0370': '6 1 3',
                '19KB1A0371': '6 1 3', '19KB1A0372': '6 1 3', '19KB1A0373': '6 1 3', '19KB1A0374': '6 1 3',
                '19KB1A0375': '6 1 3', '19KB1A0376': '6 1 3', '19KB1A0377': '6 1 3', '19KB1A0378': '6 1 3',
                '19KB1A0379': '6 1 3', '19KB1A0380': '6 1 3', '19KB1A0381': '6 1 3', '19KB1A0382': '6 1 3',
                '19KB1A0383': '6 1 3', '19KB1A0384': '6 1 3', '19KB1A0385': '6 1 3', '19KB1A0386': '6 1 3',
                '19KB1A0387': '6 1 3', '19KB1A0388': '6 1 3', '19KB1A0389': '6 1 3', '19KB1A0390': '6 1 3',
                '19KB1A0391': '6 1 3', '19KB1A0393': '6 1 3', '19KB1A0394': '6 1 3', '19KB1A0395': '6 1 3',
                '19KB1A0396': '6 1 3', '19KB1A0397': '6 1 3', '19KB1A0398': '6 1 3', '19KB1A0399': '6 1 3',
                '19KB1A03A0': '6 1 3', '19KB1A03A1': '6 1 3', '19KB1A03A2': '6 1 3', '17KB1A03B2': '6 1 3',
                '16KB1A0335': '6 1 3', '19KB1A0565': '6 2 3', '19KB1A0566': '6 2 3', '19KB1A0567': '6 2 3',
                '19KB1A0568': '6 2 3', '19KB1A0569': '6 2 3', '19KB1A0570': '6 2 3', '19KB1A0571': '6 2 3',
                '19KB1A0572': '6 2 3', '19KB1A0573': '6 2 3', '19KB1A0574': '6 2 3', '19KB1A0575': '6 2 3',
                '19KB1A0576': '6 2 3', '19KB1A0577': '6 2 3', '19KB1A0578': '6 2 3', '19KB1A0579': '6 2 3',
                '19KB1A0580': '6 2 3', '19KB1A0581': '6 2 3', '19KB1A0582': '6 2 3', '19KB1A0583': '6 2 3',
                '19KB1A0584': '6 2 3', '19KB1A0585': '6 2 3', '19KB1A0586': '6 2 3', '19KB1A0587': '6 2 3',
                '19KB1A0588': '6 2 3', '19KB1A0589': '6 2 3', '19KB1A0590': '6 2 3', '19KB1A0591': '6 2 3',
                '19KB1A0592': '6 2 3', '19KB1A0593': '6 2 3', '19KB1A0594': '6 2 3', '19KB1A0595': '6 2 3',
                '19KB1A0596': '6 2 3', '19KB1A0597': '6 2 3', '19KB1A0598': '6 2 3', '19KB1A0599': '6 2 3',
                '19KB1A05A0': '6 2 3', '19KB1A05A1': '6 2 3', '19KB1A05A2': '6 2 3', '19KB1A05A3': '6 2 3',
                '19KB1A05A4': '6 2 3', '19KB1A05A5': '6 2 3', '19KB1A05A6': '6 2 3', '19KB1A05A7': '6 2 3',
                '19KB1A05A8': '6 2 3', '19KB1A05A9': '6 2 3', '19KB1A05B0': '6 2 3', '19KB1A05B1': '6 2 3',
                '19KB1A05B2': '6 2 3', '19KB1A05B3': '6 2 3', '19KB1A05B4': '6 2 3', '19KB1A05B5': '6 2 3',
                '19KB1A05B6': '6 2 3', '19KB1A05B7': '6 2 3', '19KB1A05B8': '6 2 3', '19KB1A05B9': '6 2 3',
                '19KB1A05C0': '6 2 3', '19KB1A05C1': '6 2 3', '19KB1A05C2': '6 2 3', '19KB1A05C3': '6 2 3',
                '19KB1A05C4': '6 2 3', '19KB1A05C5': '6 2 3', '19KB1A05C6': '6 2 3', '19KB1A05C7': '6 2 3',
                '19KB1A05C8': '6 2 3', '20KB5A0507': '6 2 3', '20KB5A0508': '6 2 3', '20KB5A0509': '6 2 3',
                '20KB5A0510': '6 2 3', '20KB5A0511': '6 2 3', '20KB5A0512': '6 2 3', '19KB1A0465': '6 3 3',
                '19KB1A0466': '6 3 3', '19KB1A0467': '6 3 3', '19KB1A0468': '6 3 3', '19KB1A0469': '6 3 3',
                '19KB1A0470': '6 3 3', '19KB1A0471': '6 3 3', '19KB1A0472': '6 3 3', '19KB1A0473': '6 3 3',
                '19KB1A0474': '6 3 3', '19KB1A0475': '6 3 3', '19KB1A0476': '6 3 3', '19KB1A0477': '6 3 3',
                '19KB1A0478': '6 3 3', '19KB1A0479': '6 3 3', '19KB1A0480': '6 3 3', '19KB1A0481': '6 3 3',
                '19KB1A0482': '6 3 3', '19KB1A0483': '6 3 3', '19KB1A0484': '6 3 3', '19KB1A0485': '6 3 3',
                '19KB1A0486': '6 3 3', '19KB1A0487': '6 3 3', '19KB1A0488': '6 3 3', '19KB1A0489': '6 3 3',
                '19KB1A0490': '6 3 3', '19KB1A0491': '6 3 3', '19KB1A0492': '6 3 3', '19KB1A0493': '6 3 3',
                '19KB1A0494': '6 3 3', '19KB1A0495': '6 3 3', '19KB1A0496': '6 3 3', '19KB1A0497': '6 3 3',
                '19KB1A0498': '6 3 3', '19KB1A0499': '6 3 3', '19KB1A04A0': '6 3 3', '19KB1A04A1': '6 3 3',
                '19KB1A04A2': '6 3 3', '19KB1A04A3': '6 3 3', '19KB1A04A4': '6 3 3', '19KB1A04A5': '6 3 3',
                '19KB1A04A6': '6 3 3', '19KB1A04A7': '6 3 3', '19KB1A04A8': '6 3 3', '19KB1A04A9': '6 3 3',
                '19KB1A04B0': '6 3 3', '19KB1A04B1': '6 3 3', '19KB1A04B2': '6 3 3', '19KB1A04B3': '6 3 3',
                '19KB1A04B4': '6 3 3', '19KB1A04B5': '6 3 3', '19KB1A04B6': '6 3 3', '19KB1A04B7': '6 3 3',
                '19KB1A04B8': '6 3 3', '19KB1A04B9': '6 3 3', '19KB1A04C0': '6 3 3', '19KB1A04C1': '6 3 3',
                '19KB1A04C2': '6 3 3', '19KB1A04C3': '6 3 3', '19KB1A04C4': '6 3 3', '19KB1A04C5': '6 3 3',
                '19KB1A04C6': '6 3 3', '19KB1A04C7': '6 3 3', '19KB1A04C8': '6 3 3', '20KB5A0401': '6 3 3',
                '20KB5A0402': '6 3 3', '20KB5A0403': '6 3 3', '20KB5A0404': '6 3 3', '20KB5A0405': '6 3 3',
                '20KB5A0406': '6 3 3', '20KB5A0407': '6 3 3', '20KB5A0408': '6 3 3', '19KB1A0240': '6 4 3',
                '19KB1A0241': '6 4 3', '19KB1A0242': '6 4 3', '19KB1A0243': '6 4 3', '19KB1A0245': '6 4 3',
                '19KB1A0246': '6 4 3', '19KB1A0247': '6 4 3', '19KB1A0248': '6 4 3', '19KB1A0249': '6 4 3',
                '19KB1A0250': '6 4 3', '19KB1A0252': '6 4 3', '19KB1A0253': '6 4 3', '19KB1A0254': '6 4 3',
                '19KB1A0255': '6 4 3', '19KB1A0256': '6 4 3', '19KB1A0257': '6 4 3', '19KB1A0258': '6 4 3',
                '19KB1A0259': '6 4 3', '19KB1A0260': '6 4 3', '19KB1A0261': '6 4 3', '19KB1A0262': '6 4 3',
                '19KB1A0263': '6 4 3', '19KB1A0264': '6 4 3', '19KB1A0265': '6 4 3', '19KB1A0266': '6 4 3',
                '19KB1A0267': '6 4 3', '19KB1A0268': '6 4 3', '19KB1A0269': '6 4 3', '19KB1A0270': '6 4 3',
                '19KB1A0271': '6 4 3', '19KB1A0272': '6 4 3', '19KB1A0273': '6 4 3', '19KB1A0274': '6 4 3',
                '19KB1A0275': '6 4 3', '19KB1A0276': '6 4 3', '20KB5A0222': '6 4 3', '20KB5A0223': '6 4 3',
                '20KB5A0224': '6 4 3', '20KB5A0225': '6 4 3', '20KB5A0226': '6 4 3', '20KB5A0227': '6 4 3',
                '20KB5A0228': '6 4 3', '20KB5A0229': '6 4 3', '20KB5A0230': '6 4 3', '20KB5A0231': '6 4 3',
                '20KB5A0232': '6 4 3', '20KB5A0233': '6 4 3', '20KB5A0234': '6 4 3', '20KB5A0235': '6 4 3',
                '20KB5A0236': '6 4 3', '20KB5A0237': '6 4 3', '20KB5A0238': '6 4 3', '20KB5A0239': '6 4 3',
                '20KB5A0240': '6 4 3', '20KB5A0241': '6 4 3', '20KB5A0242': '6 4 3', '18KB5A0202': '6 4 3',
                '20KB5A0101': '6 6 3', '20KB5A0102': '6 6 3', '20KB5A0103': '6 6 3', '20KB5A0104': '6 6 3',
                '20KB5A0105': '6 6 3', '20KB5A0106': '6 6 3', '20KB5A0107': '6 6 3', '20KB5A0108': '6 6 3',
                '20KB5A0109': '6 6 3', '20KB5A0110': '6 6 3', '20KB5A0111': '6 6 3', '20KB5A0112': '6 6 3',
                '20KB5A0113': '6 6 3', '20KB5A0114': '6 6 3', '20KB5A0115': '6 6 3', '20KB5A0116': '6 6 3',
                '20KB5A0117': '6 6 3', '20KB5A0118': '6 6 3', '20KB5A0119': '6 6 3', '20KB5A0120': '6 6 3',
                '20KB5A0121': '6 6 3', '20KB5A0122': '6 6 3', '20KB5A0123': '6 6 3', '20KB5A0124': '6 6 3',
                '20KB5A0125': '6 6 3', '20KB5A0126': '6 6 3', '20KB5A0127': '6 6 3', '20KB5A0128': '6 6 3',
                '20KB5A0129': '6 6 3', '20KB5A0130': '6 6 3', '20KB5A0131': '6 6 3', '20KB5A0132': '6 6 3',
                '20KB5A0133': '6 6 3', '20KB5A0134': '6 6 3', '20KB5A0135': '6 6 3', '20KB5A0136': '6 6 3',
                '20KB5A0137': '6 6 3', '20KB5A0138': '6 6 3', '20KB5A0139': '6 6 3', '20KB5A0140': '6 6 3',
                '20KB5A0141': '6 6 3', '20KB5A0142': '6 6 3', '20KB5A0143': '6 6 3', '20KB5A0144': '6 6 3',
                '20KB5A0145': '6 6 3', '20KB5A0146': '6 6 3', '20KB5A0147': '6 6 3', '18KB1A0124': '6 6 3',
                '18KB1A0127': '6 6 3', '20KB5A0301': '6 1 4', '20KB5A0302': '6 1 4', '20KB5A0303': '6 1 4',
                '20KB5A0304': '6 1 4', '20KB5A0305': '6 1 4', '20KB5A0306': '6 1 4', '20KB5A0307': '6 1 4',
                '20KB5A0308': '6 1 4', '20KB5A0309': '6 1 4', '20KB5A0310': '6 1 4', '20KB5A0311': '6 1 4',
                '20KB5A0312': '6 1 4', '20KB5A0313': '6 1 4', '20KB5A0314': '6 1 4', '20KB5A0315': '6 1 4',
                '20KB5A0316': '6 1 4', '20KB5A0317': '6 1 4', '20KB5A0318': '6 1 4', '20KB5A0319': '6 1 4',
                '20KB5A0320': '6 1 4', '20KB5A0321': '6 1 4', '20KB5A0322': '6 1 4', '20KB5A0323': '6 1 4',
                '20KB5A0324': '6 1 4', '20KB5A0325': '6 1 4', '20KB5A0326': '6 1 4', '20KB5A0327': '6 1 4',
                '20KB5A0328': '6 1 4', '20KB5A0329': '6 1 4', '20KB5A0330': '6 1 4', '20KB5A0331': '6 1 4',
                '20KB5A0332': '6 1 4', '20KB5A0333': '6 1 4', '20KB5A0334': '6 1 4', '20KB5A0335': '6 1 4',
                '20KB5A0336': '6 1 4', '20KB5A0337': '6 1 4', '20KB5A0338': '6 1 4', '20KB5A0339': '6 1 4',
                '20KB5A0340': '6 1 4', '20KB5A0341': '6 1 4', '20KB5A0342': '6 1 4', '20KB5A0343': '6 1 4',
                '20KB5A0344': '6 1 4', '20KB5A0345': '6 1 4', '20KB5A0346': '6 1 4', '20KB5A0347': '6 1 4',
                '20KB5A0348': '6 1 4', '20KB5A0349': '6 1 4', '20KB5A0350': '6 1 4', '20KB5A0351': '6 1 4',
                '20KB5A0352': '6 1 4', '20KB5A0353': '6 1 4', '20KB5A0354': '6 1 4', '20KB5A0356': '6 1 4',
                '20KB5A0357': '6 1 4', '20KB5A0358': '6 1 4', '20KB5A0359': '6 1 4', '20KB5A0360': '6 1 4',
                '20KB5A0362': '6 1 4', '20KB5A0363': '6 1 4', '20KB5A0364': '6 1 4', '20KB5A0365': '6 1 4',
                '20KB5A0366': '6 1 4', '20KB5A0367': '6 1 4', '20KB5A0368': '6 1 4', '20KB5A0370': '6 1 4',
                '20KB5A0371': '6 1 4', '20KB5A0372': '6 1 4', '19KB1A05C9': '6 2 4', '19KB1A05D0': '6 2 4',
                '19KB1A05D1': '6 2 4', '19KB1A05D2': '6 2 4', '19KB1A05D3': '6 2 4', '19KB1A05D4': '6 2 4',
                '19KB1A05D5': '6 2 4', '19KB1A05D6': '6 2 4', '19KB1A05D7': '6 2 4', '19KB1A05D8': '6 2 4',
                '19KB1A05D9': '6 2 4', '19KB1A05E0': '6 2 4', '19KB1A05E1': '6 2 4', '19KB1A05E2': '6 2 4',
                '19KB1A05E3': '6 2 4', '19KB1A05E4': '6 2 4', '19KB1A05E5': '6 2 4', '19KB1A05E6': '6 2 4',
                '19KB1A05E7': '6 2 4', '19KB1A05E8': '6 2 4', '19KB1A05E9': '6 2 4', '19KB1A05F0': '6 2 4',
                '19KB1A05F1': '6 2 4', '19KB1A05F2': '6 2 4', '19KB1A05F3': '6 2 4', '19KB1A05F4': '6 2 4',
                '19KB1A05F5': '6 2 4', '19KB1A05F6': '6 2 4', '19KB1A05F7': '6 2 4', '19KB1A05F8': '6 2 4',
                '19KB1A05F9': '6 2 4', '19KB1A05G0': '6 2 4', '19KB1A05G1': '6 2 4', '19KB1A05G2': '6 2 4',
                '19KB1A05G3': '6 2 4', '19KB1A05G4': '6 2 4', '19KB1A05G5': '6 2 4', '19KB1A05G6': '6 2 4',
                '19KB1A05G7': '6 2 4', '19KB1A05G8': '6 2 4', '19KB1A05G9': '6 2 4', '19KB1A05H0': '6 2 4',
                '19KB1A05H1': '6 2 4', '19KB1A05H2': '6 2 4', '19KB1A05H3': '6 2 4', '19KB1A05H4': '6 2 4',
                '19KB1A05H5': '6 2 4', '19KB1A05H6': '6 2 4', '19KB1A05H7': '6 2 4', '19KB1A05H8': '6 2 4',
                '19KB1A05H9': '6 2 4', '19KB1A05I0': '6 2 4', '19KB1A05I1': '6 2 4', '19KB1A05I2': '6 2 4',
                '19KB1A05I3': '6 2 4', '19KB1A05I4': '6 2 4', '19KB1A05I5': '6 2 4', '19KB1A05I6': '6 2 4',
                '19KB1A05I7': '6 2 4', '19KB1A05I8': '6 2 4', '19KB1A05I9': '6 2 4', '19KB1A05J0': '6 2 4',
                '19KB1A05J1': '6 2 4', '19KB1A05J2': '6 2 4', '19KB1A05J3': '6 2 4', '20KB5A0513': '6 2 4',
                '20KB5A0514': '6 2 4', '20KB5A0515': '6 2 4', '20KB5A0516': '6 2 4', '20KB5A0517': '6 2 4',
                '20KB5A0518': '6 2 4', '19KB1A04C9': '6 3 4', '19KB1A04D0': '6 3 4', '19KB1A04D1': '6 3 4',
                '19KB1A04D2': '6 3 4', '19KB1A04D3': '6 3 4', '19KB1A04D4': '6 3 4', '19KB1A04D5': '6 3 4',
                '19KB1A04D6': '6 3 4', '19KB1A04D7': '6 3 4', '19KB1A04D8': '6 3 4', '19KB1A04D9': '6 3 4',
                '19KB1A04E0': '6 3 4', '19KB1A04E1': '6 3 4', '19KB1A04E2': '6 3 4', '19KB1A04E3': '6 3 4',
                '19KB1A04E4': '6 3 4', '19KB1A04E5': '6 3 4', '19KB1A04E6': '6 3 4', '19KB1A04E7': '6 3 4',
                '19KB1A04E9': '6 3 4', '19KB1A04F0': '6 3 4', '19KB1A04F1': '6 3 4', '19KB1A04F2': '6 3 4',
                '19KB1A04F3': '6 3 4', '19KB1A04F4': '6 3 4', '19KB1A04F5': '6 3 4', '19KB1A04F6': '6 3 4',
                '19KB1A04F7': '6 3 4', '19KB1A04F8': '6 3 4', '19KB1A04F9': '6 3 4', '19KB1A04G0': '6 3 4',
                '19KB1A04G1': '6 3 4', '19KB1A04G2': '6 3 4', '19KB1A04G3': '6 3 4', '19KB1A04G4': '6 3 4',
                '19KB1A04G5': '6 3 4', '19KB1A04G6': '6 3 4', '19KB1A04G7': '6 3 4', '19KB1A04G8': '6 3 4',
                '19KB1A04G9': '6 3 4', '19KB1A04H0': '6 3 4', '19KB1A04H1': '6 3 4', '19KB1A04H2': '6 3 4',
                '19KB1A04H3': '6 3 4', '19KB1A04H4': '6 3 4', '19KB1A04H5': '6 3 4', '19KB1A04H6': '6 3 4',
                '19KB1A04H7': '6 3 4', '19KB1A04H8': '6 3 4', '19KB1A04H9': '6 3 4', '19KB1A04I0': '6 3 4',
                '19KB1A04I1': '6 3 4', '19KB1A04I2': '6 3 4', '19KB1A04I3': '6 3 4', '19KB1A04I4': '6 3 4',
                '19KB1A04I5': '6 3 4', '19KB1A04I6': '6 3 4', '19KB1A04I7': '6 3 4', '19KB1A04I8': '6 3 4',
                '19KB1A04I9': '6 3 4', '19KB1A04J0': '6 3 4', '19KB1A04J1': '6 3 4', '19KB1A04J3': '6 3 4',
                '20KB5A0410': '6 3 4', '20KB5A0411': '6 3 4', '20KB5A0412': '6 3 4', '20KB5A0413': '6 3 4',
                '20KB5A0414': '6 3 4', '20KB5A0415': '6 3 4', '20KB5A0416': '6 3 4', '20KB5A0417': '6 3 4',
                '20KB5A0418': '6 3 4'}

temp_count = 0
thank_you = [ 'THANK YOU', 'TQ', 'TQ U', 'THANKS', 'THANK', 'THANK U', 'THANKYOU', 'TNQ', 'TNX' ]
options = Options()
path = '/Users/sameershaik/PycharmProjects/Checkme/static/chromedriver'
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
web = webdriver.Chrome(service=Service(os.environ.get("CHROMEDRIVER_PATH")), chrome_options=options)
web.implicitly_wait(2)

def send_to_admins():
    for admin in admins:
        try:
            WebDriverWait(web, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_aa4m _aa4p']/button"))).click()
        except:
            print('Not clickable')
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue
        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class=' _aa2u']/input"))).send_keys(admin)
        time.sleep(1)
        try:
            usern = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 "//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[1]//div[@class='_aacl _aaco _aacw _aacx _aad6']"))).text
            i = 1
            while True:
                if i == 5:
                    break
                if admin == usern:
                    WebDriverWait(web, 10).until(
                        EC.presence_of_element_located(
                            (
                            By.XPATH, f"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[{i}]"))).click()
                    break
                else:
                    usern = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         f"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[{i + 1}]//div[@class='_aacl _aaco _aacw _aacx _aad6']"))).text
                    i += 1
                    continue
        except:
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue
        try:
            time.sleep(1)
            WebDriverWait(web, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='_acan _acao _acas _acav']"))).click()
            time.sleep(1)
            send_msg(f'Hello,admin\n{len(temp_time_slot_bookings)} new subscribers\n{len(temp_register_id)} new users today')
        except:
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue



def send_att_time():
    for roll in time_slot_bookings:
        try:
            att = provide_rollno(roll)
        except:
            continue
        try:
            WebDriverWait(web, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_aa4m _aa4p']/button"))).click()
        except:
            print('Not clickable')
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue
        WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class=' _aa2u']/input"))).send_keys(roll)
        time.sleep(1)
        try:
            usern = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 "//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[1]//div[@class='_aacl _aaco _aacw _aacx _aad6']"))).text
            i = 1
            while True:
                if i == 5:
                    break
                if roll == usern:
                    WebDriverWait(web, 10).until(
                        EC.presence_of_element_located(
                            (
                            By.XPATH, f"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[{i}]"))).click()
                    break
                else:
                    usern = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         f"//div[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o  _ab9v _abcm']/div[{i + 1}]//div[@class='_aacl _aaco _aacw _aacx _aad6']"))).text
                    i += 1
                    continue
        except:
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue
        try:
            time.sleep(1)
            WebDriverWait(web, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='_acan _acao _acas _acav']"))).click()
            time.sleep(1)
            send_msg(
                f'Hello, {student_names[ register_id[ roll ] ]}\nThis Is Your Attendance Till Now: {att}\n From AttBot Subscribed Data')
        except:
            web.get('https://www.instagram.com/direct/inbox/general/')
            continue


def login(web):
    try:
        user = web.find_element(By.XPATH, '//*[@id="username"]')
        user.send_keys('rohini')
        passw = web.find_element(By.XPATH, '//*[@id="password"]')
        passw.send_keys('rohini')
        sub = web.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/form/table/tbody/tr[6]/td/input')
        sub.click()
        print("attendance site logined")
    except Exception as error:
        pass


def provide_rollno(username):
    rollno = register_id[ username ]
    att = get_data(rollno)
    return att


def get_data(rollno):
    att = None
    try:
        data = requests.get(f' https://attnbkrist1.herokuapp.com/attapi?roll={rollno}')
        data = data.json()
        att = data.get('attendance')
        return att
    except Exception as error:
        return att


def login_insta(usern, passw):
    try:
        web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usern)
        time.sleep(2)
        web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passw)
        time.sleep(2)
        web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        print('Login Successful')
    except Exception as error:
        print('Not Logined')


def not_now():
    try:
        WebDriverWait(web, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
        time.sleep(3)
        WebDriverWait(web, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//button[@class="_a9-- _a9_1"]'))).click()
        print('Not Now clicked')
    except NoSuchElementException:
        print('Not Found And passed')
        pass
    except Exception as error:
        pass


web.get('https://www.instagram.com/direct/inbox/general/')
print('Login initiated')
login_insta('attnbkrist@gmail.com', 'Nbkrist@7878')
not_now()


def read_unread_msgs():
    global temp_count,admin_count
    if (((datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour == 12) or (datetime.datetime.now(
            pytz.timezone('Asia/Kolkata')).hour == 16)) and temp_count == 0):  # checks for booking slots reservation
        send_att_time()
        print('time_slots_send')
        temp_count += 1
    elif (datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour == 13 or datetime.datetime.now(
            pytz.timezone('Asia/Kolkata')).hour == 17) and temp_count != 0:
        temp_count = 0
    elif ((datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour == 23) and admin_count == 0):  # checks for booking slots reservation
        send_to_admins()
        print('sent to admin')
        admin_count += 1
    elif ((datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour == 24) and admin_count != 0):
        admin_count = 0
    time.sleep(1)
    try:
        web.get('https://www.instagram.com/direct/requests/')
        WebDriverWait(web, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class=' _ab8s _ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm']/a"))).click()
        WebDriverWait(web, 1).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Accept')]"))).click()
        WebDriverWait(web, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_a9-z']/*[contains(text(),'General')]"))).click()
    except:
        web.get('https://www.instagram.com/direct/inbox/general/')
        try:
            WebDriverWait(web, 300).until(EC.presence_of_element_located(
                (By.XPATH, '//div[@aria-label="Unread"]'))).click()
            print('msg found')
        except:
            read_unread_msgs()


def send_msg(msg_data):
    global username, msg, msg_count
    try:
        msg_data = msg_data.replace("\n", (Keys.SHIFT + Keys.ENTER + Keys.ENTER + Keys.SHIFT))
        WebDriverWait(web, 15).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Message...']"))).send_keys(msg_data)
        time.sleep(1)
        WebDriverWait(web, 15).until(EC.presence_of_element_located((By.XPATH,
                                                                     "//button[contains(text(),'Send')]"))).click()
    except:
        username = None
        msg = None
        msg_count = 0
        print('msg send error')


def get_username():
    WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='_acan _acao _acaq _acat']"))).click()
    try:
        username = web.find_element(By.XPATH, "//h2[@class='_aacl _aacs _aact _aacx _aada']").text
    except:
        username = web.find_element(By.XPATH, "//h1[@class='_aacl _aacs _aact _aacx _aada']").text
    time.sleep(0.3)
    web.back()
    return username


temp = ''


def readmsg(oldmsg):
    global username, msg, msg_count
    count = 0
    while (True):
        time.sleep(1)
        msg = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='_acqt _acqu'])[last()]"))).text
        try:
            if msg.isdigit():
                pass
            else:
                msg = msg.upper()
        except Exception as error:
            readmsg(msg)
        if count == 30:
            send_msg('Late respose Please try after some time')
            username = None
            msg = None
            msg_count = 0
            return None
        if oldmsg == msg:
            count += 1
            continue
        else:
            break
    return msg


#web.execute_script("window.open('');")
print('Bot is Online')
read_unread_msgs()
username = None
msg = None
msg_count = 0
while (True):
    try:
        msg = readmsg(msg)
        if msg == None:
            username = None
            msg_count = 0
            read_unread_msgs()
            continue

        if not username:
            username = get_username()  # to get username
        try:
            if msg.isdigit():
                msg_count = 0
        except:
            pass
        if msg == '1':
            att = provide_rollno(username)
            send_msg(f'Hi, {student_names[ register_id[ username ] ]}\nThis is Your Attendance Till Now: {att}.')
            time.sleep(0.5)
            if username not in time_slot_bookings:
                send_msg('Type "1" If you want Again\nType "2" to Book Requests By Time')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
            else:
                send_msg('If You want again Type "1".')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
        elif msg == '2':
            if username in time_slot_bookings:
                send_msg(
                    f"Don't worry...\n{student_names[ register_id[ username ] ]}\nYou Subscribed Already.")
                username = None
                msg = None
                msg_count = 0
                read_unread_msgs()
                continue
            else:
                send_msg(
                    'Now you will get attendance twice a day automatically\n01:00 PM and 4:30 PM\nType "yes" to Confirm\nType "no" to cancel')
                msg = readmsg(msg)
                if msg == None:
                    read_unread_msgs()
                    continue
                elif msg == 'YES':
                    send_msg(f'Thanks {student_names[ register_id[ username ] ]} For Subscribe.')
                    temp_time_slot_bookings.append(username)
                    time_slot_bookings.extend(temp_time_slot_bookings)  # Extends original bbokings
                    print(temp_time_slot_bookings)  # To print in logs
                    att = provide_rollno(username)
                    send_msg(f'Attendance Till Now: {att}')
                    time.sleep(0.5)
                    msg = None
                    username = None
                    msg_count = 0
                    read_unread_msgs()
                    continue
                elif msg == 'NO':
                    send_msg('Not a Problem\nThank you')
                    username = None
                    msg = None
                    msg_count = 0
                    read_unread_msgs()
                    continue
                else:
                    send_msg("Sorry, I can't understand")
                    username = None
                    msg = None
                    msg_count = 0
                    read_unread_msgs()
                    continue
        elif msg == '3':
            send_msg('Sorry,Change option is not available')
            username = None
            msg = None
            msg_count = 0
            read_unread_msgs()
            continue
        elif msg in thank_you:
            send_msg('You are welcome')
            username = None
            msg = None
            msg_count = None
            read_unread_msgs()
            continue
        elif msg and (username not in register_id):
            if msg in student_data:
                temp_register_id[ username ] = msg
                register_id.update(temp_register_id)
                send_msg(f'Hi,{student_names[ msg ]}\nYour ROLL NO Registered Successfully')
                send_msg('Type "1" For Attendance\nType "2" to Book Requests By Time')
                continue
            else:
                send_msg('Hello, This is An Att | Bot \nPlease Enter your ROLL NO\n')
                msg = readmsg(msg)
                if msg == None:
                    read_unread_msgs()
                    continue
                if msg in student_data:
                    temp_register_id[ username ] = msg
                    register_id.update(temp_register_id)
                    send_msg(f'Hi,{student_names[ msg ]}\nYour ROLL NO Registered Successfully')
                    send_msg('Type "1" For Attendance\nType "2" to Book Requests By Time')
                    print(temp_register_id)
                    continue
                else:
                    send_msg('Roll No not available\nPlease try Again')
                    username = None
                    msg = None
                    msg_count = 0
                    read_unread_msgs()
                    continue
        elif msg == 'SEND' and username in admins:
            send_msg(
                f'You want to send att to your {len(time_slot_bookings)} subscribers\n"Yes" to confirm \n "No" to cancel')
            msg = readmsg(msg)
            if msg == 'YES':
                send_msg('Sending')
                send_att_time()
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
            elif msg == 'NO':
                send_msg('Ok, Not A Problem chinna Bot\nEnjoy pandago')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
            else:
                send_msg('Enduku Bot Time Waste Chestav\nChaduvuko First malli chudam bye')
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
        elif msg == 'C' and username in admins:
            if username == 'user_not_found_x20':
                send_msg(f"Mr Sameer\nTotal {len(register_id)} Registered users\n{len(time_slot_bookings)} subscribers")
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
            else:
                send_msg(f"Mr Arun\nTotal {len(register_id)} Registered users\n{len(time_slot_bookings)} subscribers")
                msg = None
                username = None
                msg_count = 0
                read_unread_msgs()
                continue
        elif msg == 'OK':
            send_msg('Fine')
            msg = None
            username = None
            msg_count = 0
            read_unread_msgs()
            continue
        elif username in register_id and msg and msg_count == 0:
            msg_count += 1
            send_msg(
                f'Hello,{student_names[ register_id[ username ] ]}\nYou registered already\nType "1" for Attendance\nType "2" to Book Requests By Time.')
            continue
        else:
            send_msg("Sorry, I can't understand")
            username = None
            msg = None
            msg_count = 0
            read_unread_msgs()
            continue
    except Exception as error:
        username = None
        msg = None
        msg_count = 0
        read_unread_msgs()
