#ifndef HASH_TABLE_H
#define HASH_TABLE_H

#include <stdlib.h>

// mutate typedef of key_t, object_t and hf_param_t
typedef int key_t;
typedef int object_t;
typedef int hf_param_t;

typedef struct l_node {
    key_t key;
    object_t *obj;
    struct l_node *next;
} list_node_t;
typedef struct {
    int size;
    list_node_t **table;
    int (*hash_function)(key_t, hf_param_t);
    hf_param_t hf_param;
} hashtable_t;


list_node_t *get_node() {
    list_node_t *tmp;

    tmp = (list_node_t *) malloc( sizeof(list_node_t) );
    
    return tmp;
}
void return_node(list_node_t *node) {
    free(node);
}


hashtable_t *create_hashtable(int size, int (*hash_function)(key_t, hf_param_t), hf_param_t hf_param) {
    hashtable_t *tmp;
    int i;

    tmp = (hashtable_t *) malloc( sizeof(hashtable_t) );
    tmp->size = size;
    tmp->table = (list_node_t **) malloc(size*sizeof(list_node_t *));
    tmp->hash_function = hash_function;
    tmp->hf_param = hf_param;

    for( i=0; i<size; i++ )
        (tmp->table)[i] = NULL;

    return tmp;
}
object_t *ht_find(hashtable_t *ht, key_t query_key) {
    list_node_t *tmp_node;
    int i;

    i = ht->hash_function(query_key, ht->hf_param );
    tmp_node = (ht->table)[i];

    while( tmp_node != NULL && tmp_node->key != query_key )
        tmp_node = tmp_node->next;

    if( tmp_node == NULL )
        return NULL;
    else
        return tmp_node->obj;
}
void ht_insert(hashtable_t *ht, key_t new_key, object_t *new_obj) {
    list_node_t *tmp_node;
    int i;
    
    i = ht->hash_function(new_key, ht->hf_param );
    tmp_node = (ht->table)[i];
    (ht->table)[i] = get_node();
    ((ht->table)[i])->next = tmp_node;
    ((ht->table)[i])->key = new_key;
    ((ht->table)[i])->obj = new_obj;
}
object_t *ht_delete(hashtable_t *ht, key_t del_key) {
    list_node_t *tmp_node;
    int i;

    object_t *tmp_obj;
    i = ht->hash_function(del_key, ht->hf_param );
    tmp_node = (ht->table)[i];
    if( tmp_node == NULL )
        return NULL;
    if( tmp_node->key == del_key ) {
        tmp_obj = tmp_node->obj;
        (ht->table)[i] = tmp_node->next;
        return_node( tmp_node );
        return tmp_obj;
    }

    while( tmp_node->next != NULL && tmp_node->next->key != del_key )
        tmp_node = tmp_node->next;
    if( tmp_node->next == NULL )
        return NULL;
    else {
        list_node_t *tmp_node2;
        tmp_node2 = tmp_node->next;
        tmp_node->next = tmp_node2->next;
        tmp_obj = tmp_node2->obj;
        return_node( tmp_node2 );
        return tmp_obj;
    }
}

// create your hash function or use our default function (division method)
int division_function(key_t key, hf_param_t hf_param) {
    return key % hf_param;
}

#endif