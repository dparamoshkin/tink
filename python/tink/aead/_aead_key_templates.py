# Copyright 2019 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Pre-generated KeyTemplate for Aead.

One can use these templates to generate a new tink_pb2.Keyset with
tink_pb2.KeysetHandle. To generate a new keyset that contains a single
aes_eax_pb2.AesEaxKey, one can do:
handle = keyset_handle.KeysetHandle(aead_key_templates.AES128_EAX).
"""

from __future__ import absolute_import
from __future__ import division
# Placeholder for import for type annotations
from __future__ import print_function

from tink.proto import aes_ctr_hmac_aead_pb2
from tink.proto import aes_eax_pb2
from tink.proto import aes_gcm_pb2
from tink.proto import aes_gcm_siv_pb2
from tink.proto import common_pb2
from tink.proto import tink_pb2

_AES_EAX_KEY_TYPE_URL = 'type.googleapis.com/google.crypto.tink.AesEaxKey'
_AES_GCM_KEY_TYPE_URL = 'type.googleapis.com/google.crypto.tink.AesGcmKey'
_AES_GCM_SIV_KEY_TYPE_URL = (
    'type.googleapis.com/google.crypto.tink.AesGcmSivKey')
_AES_CTR_HMAC_AEAD_KEY_TYPE_URL = (
    'type.googleapis.com/google.crypto.tink.AesCtrHmacAeadKey')
_XCHACHA20_POLY1305_KEY_TYPE_URL = (
    'type.googleapis.com/google.crypto.tink.XChaCha20Poly1305Key')


def create_aes_eax_key_template(key_size: int,
                                iv_size: int) -> tink_pb2.KeyTemplate:
  """Creates an AES EAX KeyTemplate, and fills in its values."""
  key_format = aes_eax_pb2.AesEaxKeyFormat()
  key_format.params.iv_size = iv_size
  key_format.key_size = key_size
  key_template = tink_pb2.KeyTemplate()
  key_template.value = key_format.SerializeToString()
  key_template.type_url = _AES_EAX_KEY_TYPE_URL
  key_template.output_prefix_type = tink_pb2.TINK
  return key_template


def create_aes_gcm_key_template(key_size: int) -> tink_pb2.KeyTemplate:
  """Creates an AES GCM KeyTemplate, and fills in its values."""
  key_format = aes_gcm_pb2.AesGcmKeyFormat()
  key_format.key_size = key_size
  key_template = tink_pb2.KeyTemplate()
  key_template.value = key_format.SerializeToString()
  key_template.type_url = _AES_GCM_KEY_TYPE_URL
  key_template.output_prefix_type = tink_pb2.TINK
  return key_template


def create_aes_gcm_siv_key_template(key_size: int) -> tink_pb2.KeyTemplate:
  """Creates an AES GCM SIV KeyTemplate, and fills in its values."""
  key_format = aes_gcm_siv_pb2.AesGcmSivKeyFormat()
  key_format.key_size = key_size
  key_template = tink_pb2.KeyTemplate()
  key_template.value = key_format.SerializeToString()
  key_template.type_url = _AES_GCM_SIV_KEY_TYPE_URL
  key_template.output_prefix_type = tink_pb2.TINK
  return key_template


def create_aes_ctr_hmac_aead_key_template(
    aes_key_size: int, iv_size: int, hmac_key_size: int, tag_size: int,
    hash_type: common_pb2.HashType) -> tink_pb2.KeyTemplate:
  """Creates an AES CTR HMAC AEAD KeyTemplate, and fills in its values."""
  key_format = aes_ctr_hmac_aead_pb2.AesCtrHmacAeadKeyFormat()
  key_format.aes_ctr_key_format.params.iv_size = iv_size
  key_format.aes_ctr_key_format.key_size = aes_key_size
  key_format.hmac_key_format.params.hash = hash_type
  key_format.hmac_key_format.params.tag_size = tag_size
  key_format.hmac_key_format.key_size = hmac_key_size
  key_template = tink_pb2.KeyTemplate()
  key_template.value = key_format.SerializeToString()
  key_template.type_url = _AES_CTR_HMAC_AEAD_KEY_TYPE_URL
  key_template.output_prefix_type = tink_pb2.TINK
  return key_template


AES128_EAX = create_aes_eax_key_template(key_size=16, iv_size=16)
AES256_EAX = create_aes_eax_key_template(key_size=32, iv_size=16)
AES128_GCM = create_aes_gcm_key_template(key_size=16)
AES256_GCM = create_aes_gcm_key_template(key_size=32)
AES128_GCM_SIV = create_aes_gcm_siv_key_template(key_size=16)
AES256_GCM_SIV = create_aes_gcm_siv_key_template(key_size=32)
AES128_CTR_HMAC_SHA256 = create_aes_ctr_hmac_aead_key_template(
    aes_key_size=16,
    iv_size=16,
    hmac_key_size=32,
    tag_size=16,
    hash_type=common_pb2.SHA256)
AES256_CTR_HMAC_SHA256 = create_aes_ctr_hmac_aead_key_template(
    aes_key_size=32,
    iv_size=16,
    hmac_key_size=32,
    tag_size=32,
    hash_type=common_pb2.SHA256)
XCHACHA20_POLY1305 = tink_pb2.KeyTemplate(
    type_url=_XCHACHA20_POLY1305_KEY_TYPE_URL,
    output_prefix_type=tink_pb2.TINK)
