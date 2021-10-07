#ifndef TP_INIT
#define TP_INIT

#include <stdbool.h>

#define TAPE_SIZE 1024
typedef unsigned char uchar_t;

typedef struct tape_node_t {
    uchar_t value;
    bool _visited;
    struct tape_node_t *next;
    struct tape_node_t *prev;
} tape_node_t;

/* Functions for tape_node_t */
tape_node_t *new_tape_node(uchar_t value);
void tape_node_append(tape_node_t *root, tape_node_t *node);
void tape_node_append_cyclic(tape_node_t *root, tape_node_t *node, tape_node_t *original);
void del_tape_node(tape_node_t *root);

typedef struct {
    tape_node_t *current;
} tape_t;

/* Functions for tape_t */
tape_t *new_tape(void);
void tape_ror(tape_t *tape);
void tape_rol(tape_t *tape);
void tape_set(tape_t *tape, uchar_t value);
uchar_t tape_get(tape_t *tape);
void del_tape(tape_t *tape);

#endif
