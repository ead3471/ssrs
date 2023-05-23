from typing import List, Dict


class ItemsLists:
    unit_30_items = [
        {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031FIR0001', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031TIR0001', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031PIR0001', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033FIR0001', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033TIR0005', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033PIR0001', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033FIT0319', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031FIT0105', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031FIT0147', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031FIT0155', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3031FIT0197', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032PIR0226', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032PDT0228', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033FIR0037', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033TIR0037', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3033PIR0037', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032FIR0033', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032TIR0033', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032PIR0033', 'INT_TYPE': 'a', 'GROUP_ID': '1'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032AIRA0273A', 'INT_TYPE': 'a', 'GROUP_ID': '2'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3032AIRA0273B', 'INT_TYPE': 'a', 'GROUP_ID': '2'}
        , {'NAME': 'PRODUCTION.UNIT<uid>30.<uid>3084FIR0513', 'INT_TYPE': 'i', 'GROUP_ID': '1'}
    ]

    unit_40_items = [
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FE1131', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1005', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1002', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004A', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004B', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004C', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004D', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004E', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004F', 'INT_TYPE': 'i', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004G', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004H', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1004I', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1225', 'INT_TYPE': 'i', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1225', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1225', 'INT_TYPE': 'a', 'GROUP_ID': '2'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1704A', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1704B', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1704C', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1704D', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1704E', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044FT1071', 'INT_TYPE': 'i', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044TT1071', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044PT1071', 'INT_TYPE': 'a', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044FT1108', 'INT_TYPE': 'i', 'GROUP_ID': '3'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1034A', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1034B', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1034C', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1034D', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1034E', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1034F', 'INT_TYPE': 'i', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1078', 'INT_TYPE': 'i', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1078', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1041', 'INT_TYPE': 'a', 'GROUP_ID': '4'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1040A', 'INT_TYPE': 'a', 'GROUP_ID': '5'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1040B', 'INT_TYPE': 'a', 'GROUP_ID': '5'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1040C', 'INT_TYPE': 'a', 'GROUP_ID': '5'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044FT1050', 'INT_TYPE': 'i', 'GROUP_ID': '5'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044TT1074', 'INT_TYPE': 'a', 'GROUP_ID': '5'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044PT1073', 'INT_TYPE': 'a', 'GROUP_ID': '5'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1049A', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1049B', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1049C', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1049D', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1049E', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4044AI1049F', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4081FT1011', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4081TT1011', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4081PT1011', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4090PT1013', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041EI1136G', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041EI1236G', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1142', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1139', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1047', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1240', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1239', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1090', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1533', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1030', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1225', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1130', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1230', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1097A', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1094', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1093', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1092', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1080', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041LT1083', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4081FT1013', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1095', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041LT1627', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1036', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1398', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1278', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041LT1337', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1342', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1343', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041LT1362', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1363', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1357', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1356', 'INT_TYPE': 'a', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1347', 'INT_TYPE': 'i', 'GROUP_ID': '6'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1474A', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1474B', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041AI1474C', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1212', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041TT1183', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1019', 'INT_TYPE': 'i', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1290', 'INT_TYPE': 'i', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041PT1500', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042TT1058', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042TT1048', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042TT1002', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4041FT1345', 'INT_TYPE': 'i', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042TT1055', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042LT1006', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042FT1010', 'INT_TYPE': 'i', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042PDT1078', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042AP1288', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042PT1017', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042LT1030', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042LT1037', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042PT1024', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042FT1281', 'INT_TYPE': 'i', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042PT1059', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042LT1021', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042FT1069', 'INT_TYPE': 'i', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042PT1041', 'INT_TYPE': 'a', 'GROUP_ID': '7'},
        {'NAME': 'PRODUCTION.UNIT<uid>40.<uid>4042PT1043', 'INT_TYPE': 'a', 'GROUP_ID': '7'},

    ]

    unit_50_items = [{'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051FT1007', 'INT_TYPE': ' i', 'GROUP_ID': '1'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051TT1008', 'INT_TYPE': ' a', 'GROUP_ID': '1'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051PT1006', 'INT_TYPE': ' a', 'GROUP_ID': '1'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1005A', 'INT_TYPE': ' a', 'GROUP_ID': '2'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1005B', 'INT_TYPE': ' a', 'GROUP_ID': '2'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1005D', 'INT_TYPE': ' a', 'GROUP_ID': '2'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051FT1018', 'INT_TYPE': ' a', 'GROUP_ID': '2'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1016A', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1016B', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1016C', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1016D', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1016E', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051TT1020', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AP1058', 'INT_TYPE': ' a', 'GROUP_ID': '3'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1021A', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1021B', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AI1021C', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051LT1032', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051TT1035', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051FT1064', 'INT_TYPE': ' i', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051PT1066', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051PT1048', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AP1046', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051AP1047', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051PT1052', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051FT1036', 'INT_TYPE': ' i', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051PT1037', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051FT1062', 'INT_TYPE': ' i', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PT1129', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051PT1056', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051TT1042', 'INT_TYPE': ' a', 'GROUP_ID': '4'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1108A', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1108B', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1108C', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1108D', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1108E', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5051TT1041', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1068', 'INT_TYPE': ' i', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PT1068', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TT1068', 'INT_TYPE': ' a', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1133A', 'INT_TYPE': ' i', 'GROUP_ID': '5'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AP1019A', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AP1019B', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AP1019C', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AP1019D', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AP1019E', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TT1005', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1085', 'INT_TYPE': ' i', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PT1084', 'INT_TYPE': ' a', 'GROUP_ID': '6'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1136A', 'INT_TYPE': ' a', 'GROUP_ID': '7'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1136F', 'INT_TYPE': ' a', 'GROUP_ID': '7'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1101', 'INT_TYPE': ' i', 'GROUP_ID': '7'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PT1100', 'INT_TYPE': ' a', 'GROUP_ID': '7'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1099A', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1099B', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1099C', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1099D', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1099E', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PC1092', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052LT1035', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052LT1137', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TT1118', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PT1039', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1040A', 'INT_TYPE': ' i', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TI1116', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052LT1037', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TI1062', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TT1077', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052TI1054', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1055A', 'INT_TYPE': ' i', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1055B', 'INT_TYPE': ' i', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052PT1031A', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052LT1028', 'INT_TYPE': ' a', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1032', 'INT_TYPE': ' i', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1033', 'INT_TYPE': ' i', 'GROUP_ID': '8'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1112A', 'INT_TYPE': ' a', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1112B', 'INT_TYPE': ' a', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052FT1110', 'INT_TYPE': ' i', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053PT1002', 'INT_TYPE': ' a', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053FT1003', 'INT_TYPE': ' i', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053PT5006', 'INT_TYPE': ' a', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053PT5406', 'INT_TYPE': ' a', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053FT1017', 'INT_TYPE': ' i', 'GROUP_ID': '9'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1115B', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1115D', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5052AI1115H', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053PT1040', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053TT1066', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5053PT1026', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5054PT5200', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5054PT5316', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5055WT5810', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5056PT1009', 'INT_TYPE': ' a', 'GROUP_ID': '10'},
                     {'NAME': 'PRODUCTION.UNIT<uid>50.<uid>5056FT1003', 'INT_TYPE': ' i', 'GROUP_ID': '10'},
                     ]

    unit_tsb_items = [
        {'NAME': 'TANKFARM.03176LI0001A', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002A', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001B', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002B', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001C', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002C', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001D', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002D', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001E', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002E', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001F', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002F', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001G', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002G', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LI0001H', 'INT_TYPE': 's', 'GROUP_ID': '1'}
        , {'NAME': 'TANKFARM.03176LZIA0002H', 'INT_TYPE': 's', 'GROUP_ID': '1'}

        , {'NAME': 'TANKFARM.03276LI0001A', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LZIA0002A', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LI0001B', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LZIA0002B', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LI0001C', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LZIA0002C', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LI0001D', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LZIA0002D', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LI0008A', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LZIA0006A', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LI0008B', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03276LZIA0006B', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03275LI0011A', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03275LI0013A', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03275LI0011B', 'INT_TYPE': 's', 'GROUP_ID': '2'}
        , {'NAME': 'TANKFARM.03275LI0013B', 'INT_TYPE': 's', 'GROUP_ID': '2'}

        , {'NAME': 'TANKFARM.03376LI0003A', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LZIA0001A', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LI0003B', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LZIA0001B', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LI0003C', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LZIA0001C', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LI0003D', 'INT_TYPE': 's', 'GROUP_ID': '3'}
        , {'NAME': 'TANKFARM.03376LZIA0001D', 'INT_TYPE': 's', 'GROUP_ID': '3'}

        , {'NAME': 'PRODUCTION.UNIT150.15055LI5001', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5001A', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5001B', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LI5101', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5101A', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5101B', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LI5201', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5201A', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5201B', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LI5301', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5301A', 'INT_TYPE': 's', 'GROUP_ID': '4'}
        , {'NAME': 'PRODUCTION.UNIT150.15055LR5301B', 'INT_TYPE': 's', 'GROUP_ID': '4'}

        , {'NAME': 'PRODUCTION.UNIT250.25055LI5001', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5001A', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5001B', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LI5101', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5101A', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5101B', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LI5201', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5201A', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5201B', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LI5301', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5301A', 'INT_TYPE': 's', 'GROUP_ID': '5'}
        , {'NAME': 'PRODUCTION.UNIT250.25055LR5301B', 'INT_TYPE': 's', 'GROUP_ID': '5'}

        , {'NAME': 'PRODUCTION.UNIT350.35055LI5001', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5001A', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5001B', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LI5101', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5101A', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5101B', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LI5201', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5201A', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5201B', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LI5301', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5301A', 'INT_TYPE': 's', 'GROUP_ID': '6'}
        , {'NAME': 'PRODUCTION.UNIT350.35055LR5301B', 'INT_TYPE': 's', 'GROUP_ID': '6'}

    ]

    unit_110_items = [
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110AFIR0051', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110ATIR0051', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110APIR0051', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BFIR0051', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BTIR0051', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BPIR0051', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110AFIR0062', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110ATIR0062', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110APIR0062', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BFIR0062', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BTIR0062', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BPIR0062', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110AFIR0067', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110ATIR0067', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110APIR0067', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BFIR0063', 'INT_TYPE': 'i', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BTIR0063', 'INT_TYPE': 'a', 'GROUP_ID': '1'},
        {'NAME': 'PRODUCTION.UNIT<uid>110.<uid>110BPIR0063', 'INT_TYPE': 'a', 'GROUP_ID': '1'},

    ]

    unit_names_map = {'unit_30': unit_30_items,
                      'unit_40': unit_40_items,
                      'unit_50': unit_50_items,
                      'unit_tsb': unit_tsb_items,
                      'unit_110':unit_110_items}

    @staticmethod
    def get_unit_items(unit_name: str, unit_id: str) -> List[Dict]:
        """
        used for retrieve report items for required unit

        :param unit_name: name of unit
        :param unit_id: unit number
        :return:
        list of report items for given unit_name and unit_id
        """
        if unit_name not in ItemsLists.unit_names_map:
            raise ValueError(f"Bad unit name(not in accepted list):{unit_name}")

        if unit_id == '':
            return ItemsLists.unit_names_map[unit_name]
        else:
            result_list = ItemsLists.unit_names_map[unit_name]
            for item in result_list:
                item['NAME'] = str(item['NAME']).replace('<uid>', unit_id)
            return result_list
