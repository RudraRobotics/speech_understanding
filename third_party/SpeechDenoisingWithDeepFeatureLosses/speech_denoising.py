from model import *
from data_import import *

import sys, getopt

class SpeechDenoising():
    def __init__(self, args):
        # SPEECH ENHANCEMENT NETWORK
        self.SE_LAYERS = args.se_layers # 13 # NUMBER OF INTERNAL LAYERS
        self.SE_CHANNELS = args.se_channels # 64 # NUMBER OF FEATURE CHANNELS PER LAYER
        self.SE_LOSS_LAYERS = args.se_loss_layers # 6 # NUMBER OF FEATURE LOSS LAYERS
        self.SE_NORM = args.se_norm # "NM" # TYPE OF LAYER NORMALIZATION (NM, SBN or None)
        self.fs = args.fs # 16000

        # SET LOSS FUNCTIONS AND PLACEHOLDERS
        with tf.variable_scope(tf.get_variable_scope()):
            input=tf.placeholder(tf.float32,shape=[None,1,None,1])
            clean=tf.placeholder(tf.float32,shape=[None,1,None,1])        
            enhanced=senet(input, n_layers=self.SE_LAYERS, norm_type=self.SE_NORM, n_channels=self.SE_CHANNELS)

        if arg.load_static_data is True:
            # LOAD DATA
            self.valset = load_noisy_data_list(valfolder = valfolder)
            self.valset = load_noisy_data(valset)

        # INITIALIZE GPU CONFIG
        config=tf.ConfigProto()
        config.gpu_options.allow_growth=True
        self.sess=tf.Session(config=config)

        print "Config ready"

        self.sess.run(tf.global_variables_initializer())

        print "Session initialized"

        saver = tf.train.Saver([var for var in tf.trainable_variables() if var.name.startswith("se_")])
        saver.restore(sess, "./%s/se_model.ckpt" % modfolder)

    '''
    Function to remove noise from given noisy audio
    Input: noisy audio raw data
    Output: denoised audio raw data in numpy format
    '''
    def get_denoised_audio(self, noisy_audio):
        # VALIDATION ITERATION
        denoised_audio = self.sess.run([enhanced], feed_dict={input: noisy_audio})
        denoised_audio = np.reshape(denoised_audio, -1)
        return denoised_audio


