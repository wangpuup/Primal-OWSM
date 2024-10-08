#!/usr/bin/env python3
from espnet2.tasks.s2t_primal import S2TPRIMALTask


def get_parser():
    parser = S2TPRIMALTask.get_parser()
    return parser


def main(cmd=None):
    r"""ASR training.

    Example:

        % python asr_train.py asr --print_config --optim adadelta \
                > conf/train_asr.yaml
        % python asr_train.py --config conf/train_asr.yaml
    """
    S2TPRIMALTask.main(cmd=cmd)


if __name__ == "__main__":
    main()
