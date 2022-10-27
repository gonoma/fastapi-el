# coding: utf-8
from fastapi import APIRouter, Depends

router = APIRouter()


# @router.post(
#     "/results",
#     dependencies=[Depends(existing_user)],
#     response_model=models.responses.Results
# )
# def post_test_results(
#         results: dict,
#         db: Session = Depends(get_db)
# ) -> database.schemas.tests.Results:
#     """
#     Persist into the DB the results of the reading test
#
#     :param results: dict with reading test results
#     :type results: dict
#     :param db: Database Session
#     :type db: Session
#     :return: database.schemas.tests.Results
#     """
#
#     return 1
