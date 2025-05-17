config_dict = {
    "datasphere_prefix": '/home/jupyter/work/resources/DiplomDimReduction/',
    "google_prefix": '/content/drive/MyDrive/Colab Notebooks/Diplom',
    "data_prefix": "data",
    "raw_prefix": "raw",
    "vectors_prefix": "vectors",
    "models_prefix": "models",
    "marco_prefix": "marco",
    "dpr_prefix": "dpr",
    "ance_prefix": "ance",
    "tas-b_prefix": "tas_b",
    "late interaction prefix": "colbert",
    "re-ranking prefix": "re_ranking",

    "train_suffix": "train",
    "val_suffix": "validation",
    "test_suffix": "test",

    "marco_name": 'BeIR/msmarco',
    "marco_qrels_name": 'BeIR/msmarco-qrels',

    'dpr_model': 'facebook/dpr-question_encoder-multiset-base',
    "ance_model": "sentence-transformers/msmarco-roberta-base-ance-firstp",
    "tas-b_model": "sentence-transformers/msmarco-distilbert-base-tas-b",
    'colbert_model': 'colbert-ir/colbertv2.0',
    "ce_model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
}

# СЫРЫЕ ДАННЫЕ
config_dict['corpus_data_template'] = (config_dict['datasphere_prefix'] + '/' +
                                       config_dict['data_prefix'] + '/' +
                                       config_dict['raw_prefix'] + '/' +
                             '{}/corpus.parquet'  # корпус + колонка
                                       )
config_dict['corpus_ids_template'] = (config_dict['datasphere_prefix'] + '/' +
                                      config_dict['data_prefix'] + '/' +
                                      config_dict['raw_prefix'] + '/' +
                             '{}/corpus.json'  # корпус + колонка
                                      )

config_dict['queries_data_template'] = (config_dict['datasphere_prefix'] + '/' +
                                        config_dict['data_prefix'] + '/' +
                                        config_dict['raw_prefix'] + '/' +
                             '{}/queries.parquet'  # корпус + колонка
                                        )
config_dict['queries_ids_template'] = (config_dict['datasphere_prefix'] + '/' +
                                       config_dict['data_prefix'] + '/' +
                                       config_dict['raw_prefix'] + '/' +
                             '{}/queries.json'  # корпус + колонка
                                       )

config_dict['qrels_data_template'] = (config_dict['datasphere_prefix'] + '/' +
                                      config_dict['data_prefix'] + '/' +
                                      config_dict['raw_prefix'] + '/' +
                             '{}/qrels_{}.parquet'  # корпус + колонка_сплит
                                      )

config_dict['data_ids_template'] = (config_dict['datasphere_prefix'] + '/' +
                                config_dict['data_prefix'] + '/' +
                                config_dict['raw_prefix'] + '/' +
                             '{}/data_{}.json'  # корпус + колонка_сплит
                                      )

config_dict['data_template'] = (config_dict['datasphere_prefix'] + '/' +
                                config_dict['data_prefix'] + '/' +
                                config_dict['raw_prefix'] + '/' +
                             '{}/data_{}.parquet'  # корпус + колонка_сплит
                                      )


# ВЕКТОРА
config_dict['corpus_vector_template'] = (config_dict['datasphere_prefix'] + '/' +
                                         config_dict['data_prefix'] + '/' +
                                         config_dict['vectors_prefix'] + '/' +
                             '{}/{}/corpus_{}.npz'  # корпус + метод + колонка_сплит
                                         )
config_dict['corpus_mapping_template'] = (config_dict['datasphere_prefix'] + '/' +
                                         config_dict['data_prefix'] + '/' +
                                         config_dict['vectors_prefix'] + '/' +
                             '{}/{}/corpus_{}.json'  # корпус + метод + колонка_сплит
                                         )
config_dict['corpus_sample_vector_template'] = (config_dict['datasphere_prefix'] + '/' +
                                         config_dict['data_prefix'] + '/' +
                                         config_dict['vectors_prefix'] + '/' +
                             '{}/{}/corpus_{}_sample.npz'  # корпус + метод + колонка_сплит_семпл
                                         )


config_dict['queries_vector_template'] = (config_dict['datasphere_prefix'] + '/' +
                                          config_dict['data_prefix'] + '/' +
                                          config_dict['vectors_prefix'] + '/' +
                             '{}/{}/queries_{}.npz'  # корпус + метод + колонка_сплит
                                          )
config_dict['queries_mapping_template'] = (config_dict['datasphere_prefix'] + '/' +
                                          config_dict['data_prefix'] + '/' +
                                          config_dict['vectors_prefix'] + '/' +
                             '{}/{}/queries_{}.json'  # корпус + метод + колонка_сплит
                                          )


# МОДЕЛИ
config_dict['reduction_sk_model_template'] = (config_dict['datasphere_prefix'] + '/' +
                                          config_dict['data_prefix'] + '/' +
                                          config_dict['models_prefix'] + '/' +
                             '{}/{}/{}_{}.joblib'  # корпус + метод + модель_размерность
                                          )

config_dict['reduction_ae_model_template'] = (config_dict['datasphere_prefix'] + '/' +
                                          config_dict['data_prefix'] + '/' +
                                          config_dict['models_prefix'] + '/' +
                             '{}/{}/{}_{}.pt'  # корпус + метод + модель_размерность
                                          )
