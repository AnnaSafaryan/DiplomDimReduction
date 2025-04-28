config_dict = {
    "google_prefix": '/content/drive/MyDrive/Colab Notebooks/Diplom',
    "data_prefix": "data",
    "raw_prefix": "raw",
    "marco_prefix": "marco",
    "dpr_prefix": "dpr",
    "ance_prefix": "ance",
    "tas-b_prefix": "tas_b",
    "late interaction prefix": "late_interaction",
    "re-ranking prefix": "re_ranking",

    "marco_name": 'BeIR/msmarco',
    "marco_qrels_name": 'BeIR/msmarco-qrels',

    'dpr_model': 'facebook/dpr-question_encoder-multiset-base',
    "ance_model": "sentence-transformers/msmarco-roberta-base-ance-firstp",
    "tas-b_model": "sentence-transformers/msmarco-distilbert-base-tas-b",
    'colbert_model': 'colbert-ir/colbertv2.0',
    "ce_model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
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
