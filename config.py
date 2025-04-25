config_dict = {
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

    "marco_name": 'BeIR/msmarco',
    "marco_qrels_name": 'BeIR/msmarco-qrels',

    
    'dpr_model': 'facebook/dpr-question_encoder-multiset-base',
    'colbert_model': 'colbert-ir/colbertv2.0',
    "ce_model": "cross-encoder/ms-marco-MiniLM-L-6-v2"

}

# СЫРЫЕ ДАННЫЕ
config_dict['corpus_data_template'] = (config_dict['google_prefix'] + '/' +
                                       config_dict['data_prefix'] + '/' +
                                       config_dict['raw_prefix'] + '/' +
                             '{}/corpus_test.parquet'  # корпус + колонка_сплит
                                       )
config_dict['corpus_ids_template'] = (config_dict['google_prefix'] + '/' +
                                      config_dict['data_prefix'] + '/' +
                                      config_dict['raw_prefix'] + '/' +
                             '{}/corpus_test.json'  # корпус + колонка_сплит
                                      )

config_dict['queries_data_template'] = (config_dict['google_prefix'] + '/' +
                                        config_dict['data_prefix'] + '/' +
                                        config_dict['raw_prefix'] + '/' +
                             '{}/queries_test.parquet'  # корпус + колонка_сплит
                                        )
config_dict['queries_ids_template'] = (config_dict['google_prefix'] + '/' +
                                       config_dict['data_prefix'] + '/' +
                                       config_dict['raw_prefix'] + '/' +
                             '{}/queries_test.json'  # корпус + колонка_сплит
                                       )

config_dict['qrels_data_template'] = (config_dict['google_prefix'] + '/' +
                                      config_dict['data_prefix'] + '/' +
                                      config_dict['raw_prefix'] + '/' +
                             '{}/qrels_test.parquet'  # корпус + колонка_сплит
                                      )

config_dict['data_template'] = (config_dict['google_prefix'] + '/' +
                                      config_dict['data_prefix'] + '/' +
                                      config_dict['raw_prefix'] + '/' +
                             '{}/data_test.parquet'  # корпус + колонка_сплит
                                      )

# ВЕКТОРА
config_dict['corpus_vector_template'] = (config_dict['google_prefix'] + '/' +
                                         config_dict['data_prefix'] + '/' +
                                         config_dict['vectors_prefix'] + '/' +
                             '{}/{}/corpus_test.npz'  # метод + корпус + колонка_сплит
                                         )
config_dict['corpus_mapping_template'] = (config_dict['google_prefix'] + '/' +
                                         config_dict['data_prefix'] + '/' +
                                         config_dict['vectors_prefix'] + '/' +
                             '{}/{}/corpus_test.json'  # метод + корпус + колонка_сплит
                                         )


config_dict['queries_vector_template'] = (config_dict['google_prefix'] + '/' +
                                          config_dict['data_prefix'] + '/' +
                                          config_dict['vectors_prefix'] + '/' +
                             '{}/{}/queries_test.npz'  # метод + корпус + колонка_сплит
                                          )
config_dict['queries_mapping_template'] = (config_dict['google_prefix'] + '/' +
                                          config_dict['data_prefix'] + '/' +
                                          config_dict['vectors_prefix'] + '/' +
                             '{}/{}/queries_test.json'  # метод + корпус + колонка_сплит
                                          )
