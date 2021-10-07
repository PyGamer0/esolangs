#include <stdlib.h>

#include "tape.h"

/* Tape node functions */
tape_node_t *new_tape_node(uchar_t value) {
    tape_node_t *node = (tape_node_t *) malloc(sizeof(tape_node_t));
    node->value = value;
    node->next = NULL;
    node->prev = NULL;
    node->_visited = false;
    return node;
}

void tape_node_append(tape_node_t *root, tape_node_t *node) {
    if (root->next == NULL) {
        root->next = node;
        node->prev = root;
    } else {
        tape_node_append(root->next, node);
    }
}

void tape_node_append_cyclic(tape_node_t *root, tape_node_t *node, tape_node_t *original) {
    if (root->next == NULL) {
        root->next = node;
        node->prev = root;

        node->next = original;
        original->prev = node;
    } else {
        tape_node_append_cyclic(root->next, node, original);
    }
}

void del_tape_node(tape_node_t *root) {
    if (root == NULL || root->_visited)
        return;
    root->_visited = true;
    del_tape_node(root->next);
    free(root);
}

/* Tape functions */
tape_t *new_tape() {
    tape_t *tape = (tape_t *) malloc(sizeof(tape_t));
    tape->current = new_tape_node(0);
    for (int i = 0; i < TAPE_SIZE - 2; i++) {
        tape_node_append(tape->current, new_tape_node(0));
    }
    tape_node_append_cyclic(tape->current, new_tape_node(0), tape->current);
    return tape;
}

void tape_ror(tape_t *tape) {
    tape->current = tape->current->next;
}

void tape_rol(tape_t *tape) {
    tape->current = tape->current->prev;
}

void tape_set(tape_t *tape, uchar_t value) {
    tape->current->value = value;
}

uchar_t tape_get(tape_t *tape) {
    return tape->current->value;
}

void del_tape(tape_t *tape) {
    del_tape_node(tape->current);
    free(tape);
}
