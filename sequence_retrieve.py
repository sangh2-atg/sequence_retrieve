from urllib import request
import os

base_url = r'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'

def retrieve_multiple_seq(gb_id_list, save_name, rettype='fasta', retmode='text', save_path=''):
    gb_id_str = str()
    for gb_id in gb_id_list:
        if bool(gb_id_str) is False:
            gb_id_str = gb_id
        else:
            gb_id_str = f'{gb_id_str},{gb_id}'

    if bool(save_path) is True:
        d_ = os.path.join(save_path, f'{save_name}.{rettype}')
    else:
        d_ = f'{save_name}.{rettype}'
    url = f"{base_url}?db=nuccore&id={gb_id_str}&rettype={rettype}&retmode={retmode}"
    request.urlretrieve(url, d_)

def retrieve_single_seq(gb_id, rettype='fasta', retmode='text', save_path='', seq_start=0, seq_stop=0):

    if bool(save_path) is True:
        d_ = os.path.join(save_path, f'{gb_id}.{rettype}')
    else:
        d_ = f'{gb_id}.{rettype}'

    if bool(seq_start) is False and bool(seq_stop) is False:
        url = f"{base_url}?db=nuccore&id={gb_id}&rettype={rettype}&retmode={retmode}"
        request.urlretrieve(url, d_)
    elif bool(seq_start) is True and bool(seq_stop) is False:
        url = f"{base_url}?db=nuccore&id={gb_id}&rettype={rettype}&retmode={retmode}&seq_start={seq_start}"
        request.urlretrieve(url, d_)
    elif bool(seq_start) is False and bool(seq_stop) is True:
        url = f"{base_url}?db=nuccore&id={gb_id}&rettype={rettype}&retmode={retmode}&seq_stop={seq_stop}"
        request.urlretrieve(url, d_)
    elif bool(seq_start) is True and bool(seq_stop) is True:
        url = f"{base_url}?db=nuccore&id={gb_id}&rettype={rettype}&retmode={retmode}&seq_start={seq_start}&seq_stop={seq_stop}"
        request.urlretrieve(url, d_)
