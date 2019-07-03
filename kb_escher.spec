/*
A KBase module: kb_escher
*/

module kb_escher {

    funcdef list_maps(mapping<string,UnspecifiedObject> params) returns (mapping<string,UnspecifiedObject> output);
    funcdef list_models(mapping<string,UnspecifiedObject> params) returns (mapping<string,UnspecifiedObject> output);
    funcdef get_model(mapping<string,UnspecifiedObject> params) returns (mapping<string,UnspecifiedObject> output);
    funcdef get_map(mapping<string,UnspecifiedObject> params) returns (mapping<string,UnspecifiedObject> output);
};
