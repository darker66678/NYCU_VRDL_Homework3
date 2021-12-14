if [ $1 == "train" ]; then
    python tools/train.py ./train_config/config.py
elif [ $1 == "test" ]; then
    python tools/test.py ./train_config/config.py $2  --format-only --options "jsonfile_prefix=./results" --out prediction.pkl
elif [ $1 == "show" ]; then
    python tools/test.py ./train_config/config.py $2  --show
fi

