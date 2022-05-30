# documents_ci = []
# documents_ca_cm = []
#
# queries_ci = []

import IR_Project.utils.document.parser_ci as ci_document
import IR_Project.utils.document.parser_ci as ci_query
import IR_Project.utils.document.parser_cacm as ca_cm_document

documents_ci = ci_document.parse_ci_all()
documents_ca_cm = ca_cm_document.parse_ca_cm_all()
queries_ci = ci_query.parse_ci_all()
