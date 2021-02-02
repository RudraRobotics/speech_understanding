#
#    Copyright 2018 Picovoice Inc.
#
#    You may not use this file except in compliance with the license. A copy of the license is located in the "LICENSE"
#    file accompanying this source.
#
#    Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
#    an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
#    specific language governing permissions and limitations under the License.
#

import os
import sys

import soundfile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../binding/python'))

from leopard import Leopard


if __name__ == '__main__':

    leopard = Leopard(
        library_path='/home/ubuntu/Downloads/leopard/lib/linux/x86_64/libpv_leopard.so',
        acoustic_model_path='/home/ubuntu/Downloads/leopard/lib/common/acoustic_model.pv',
        language_model_path='/home/ubuntu/Downloads/leopard/lib/common/language_model.pv',
        license_path='/home/ubuntu/Downloads/leopard/resources/license/license_leo_v1.0.0_linux_expires_3_4_2021.lic')

    audio_path='/home/ubuntu/Downloads/leopard/resources/audio_samples/test.wav'
    audio, sample_rate = soundfile.read(audio_path, dtype='int16')
    if sample_rate != leopard.sample_rate:
        raise ValueError('Leopard can only process audio data with sample rate of %d' % leopard.sample_rate)
    transcript = leopard.process(audio)

    print(transcript)

