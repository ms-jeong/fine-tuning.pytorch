# Configuration File

# Base directory for data formats
#name = 'INBREAST_5'
#test_dir = '/home/bumsoo/Data/test/FINAL_HWEJIN/HWEJIN_INBREAST_SPLIT'

#name = 'GURO_CELL'
#test_dir = '/home/bumsoo/Data/split/GURO_CELL/val/'

# INBREAST
#name = 'INBREAST_TRAIN'
#test_dir = '/home/bumsoo/Data/test/HWEJIN_INBREAST_SPLIT'

# GURO_SPLIT
name = 'GURO_TRAIN'
#test_dir = '/home/bumsoo/Data/test/FINAL_HWEJIN/HWEJIN_GURO_SPLIT'

# GURO_ALL -> INBREAST_ALL
#name = 'GURO_ALL'
#test_dir = '/home/bumsoo/Data/test/FINAL_HWEJIN/INBREAST_ALL'

# MIX_TRAIN -> MIX_TEST
#name = 'MIX_TRAIN'
#test_dir = '/home/bumsoo/Data/test/FINAL_HWEJIN/HWEJIN_MIX_TEST'
test_dir = '/home/bumsoo/inference_patches/guro_patches_test_8'

# GURO80+INBREAST_ALL
#name = 'GURO80+INBREAST'
#test_dir = '/home/bumsoo/Data/test/FINAL_HWEJIN/GURO80+INBREAST'

# INBREAST80+GURO_ALL
#name = 'INBREAST80+GURO'
#test_dir = '/home/bumsoo/Data/test/FINAL_HWEJIN/INBREAST80+GURO'

# Inference (INBREAST_test)
#name = 'INBREAST_TRAIN'
#test_dir = '/home/bumsoo/Data/test/inbreast_patches_test_9'
#test_dir = '/mnt/datasets/inbreast_patches_test_9'

# Inference (GURO_test)
#name = 'GURO_TRAIN'
#test_dir = '/home/bumsoo/Data/test/guro_patches_test_0'
#test_dir = '/home/bumsoo/guro_patches_test_9'

# Inference (GURO_ALL -> INBREAST_ALL)
#name = 'GURO_ALL'
#test_dir = '/home/bumsoo/Data/test/PATCH_INBREAST_TEST/inbreast_patches_4'

data_base = '/home/mnt/datasets/'+name
aug_base = '/home/bumsoo/Data/split/'+name

# model option
batch_size = 16
num_epochs = 50
lr_decay_epoch=20
feature_size = 500

# meanstd options
# INBREAST_SPLIT
#mean = [0.601176900699946, 0.601176900699946, 0.601176900699946]
#std = [0.083943294373731825, 0.083943294373731825, 0.083943294373731825]

# GURO_SPLIT
#mean = [0.49113493759286625, 0.49113493759286625, 0.49113493759286625]
#std = [0.14704804249157166, 0.14704804249157166, 0.14704804249157166]

# GURO_ALL
#mean = [0.42641446119819587, 0.42641446119819587, 0.42641446119819587]
#std = [0.19647293715592193, 0.19647293715592193, 0.19647293715592193]

# GURO+INBREAST
#mean = [0.53753781240686382, 0.53753781240686382, 0.53753781240686382]
#std = [0.12187187243213095, 0.12187187243213095, 0.12187187243213095]

# MIX_TRAIN
#mean = [0.50528327792298555, 0.50528327792298555, 0.50528327792298555]
#std = [0.13993786443871117, 0.13993786443871117, 0.13993786443871117]

# GURO80+INBREAST_ALL
#mean = [0.49977846189176656, 0.49977846189176656, 0.49977846189176656]
#std = [0.14111615457915755, 0.14111615457915755, 0.14111615457915755]

# INBREAST80+GURO_ALL
mean = [0.4856586910840433, 0.4856586910840433, 0.4856586910840433]
std = [0.14210993338737993, 0.14210993338737993, 0.14210993338737993]

# GURO_CELL
#mean = [0.78076776409256798, 0.61738499185119988, 0.62287074541563914]
#std = [0.18391759503019442, 0.26082926658759176, 0.23288027411260487]

# INBREAST_1
#mean = [0.60284723168105081, 0.60284723168105081, 0.60284723168105081]
#std = [0.081163047606150382, 0.081163047606150382, 0.081163047606150382]

# INBREAST_2
#mean = [0.61158796966756579, 0.61158796966756579, 0.61158796966756579]
#std = [0.08487070239187032, 0.08487070239187032, 0.08487070239187032]

# INBREAST_3
#mean = [0.60108720150874573, 0.60108720150874573, 0.60108720150874573]
#std = [0.081551750213639501, 0.081551750213639501, 0.081551750213639501]

# INBREAST_4
#mean = [0.60402172760178874, 0.60402172760178874, 0.60402172760178874]
#std = [0.078366899563820674, 0.078366899563820674, 0.078366899563820674]

# INBREAST_5
#mean = [0.59631095620282071, 0.59631095620282071, 0.59631095620282071]
#std = [0.080351500548752522, 0.080351500548752522, 0.080351500548752522]
