config = {
    "google_prefix": '/content/drive/MyDrive/Colab Notebooks/Diplom',
    "data_prefix": "data",
    "raw_prefix": "raw",
    "vectors_prefix": "vectors",
    "marco_prefix": "marco",
    "dpr_prefix": "dpr",
    "ance_prefix": "ance",
    "tab-s_prefix": "tab_s",
    "late interaction prefix": "late_interaction",
    "re-ranking prefix": "re_ranking",
}

# СЫРЫЕ ДАННЫЕ
config['corpus_data_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['raw_prefix'] + '/' +
                             '{}/corpus_test.parquet' # корпус + колонка_сплит
                             )
config['corpus_ids_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['raw_prefix'] + '/' +
                             '{}/corpus_test.json' # корпус + колонка_сплит
                             )

config['queries_data_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['raw_prefix'] + '/' +
                             '{}/queries_test.parquet' # корпус + колонка_сплит
                             )
config['corpus_ids_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['raw_prefix'] + '/' +
                             '{}/queries_test.json' # корпус + колонка_сплит
                             )

config['qrels_data_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['raw_prefix'] + '/' +
                             '{}/qrels_test.parquet' # корпус + колонка_сплит
                             )


# ВЕКТОРА
config['corpus_vector_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['vectors_prefix'] + '/' +
                             '{}/{}/corpus_test.npz' # метод + корпус + колонка_сплит
                             )
config['queries_vector_template'] = (config['google_prefix'] + '/' +
                             config['data_prefix'] + '/' +
                             config['vectors_prefix'] + '/' +
                             '{}/{}/queries_test.npz' # метод + корпус + колонка_сплит
                             )

# print(config)