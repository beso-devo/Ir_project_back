import IR_Project.utils.document.parser_ci as ci_document
import IR_Project.utils.document.parser_cacm as ca_cm_document
import IR_Project.models.document_cacm
import IR_Project.utils.query.query_parser_cisi as ci_query

import IR_Project.utils.results.result_ci_parser as ci_result

documents_ci = ci_document.parse_ci_all()
documents_ca_cm = ca_cm_document.parse_ca_cm_all()

queries_ci = ci_query.parse_ci_si_query_all()

# queries_ci = []
results_ci = []
