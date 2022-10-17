from uuid import UUID

from models.account import Account, UserData, Contacts
from repositories.accounts_repository import create_account, get_account_by_username, get_account_by_id, delete_account_by_id


class TestAccountsRepository:
    def test_accounts_db(self):
        account_username: str = "test_account"

        # test creation
        account_id = create_account(
            account_username,
            UserData.mock(),
            Contacts.mock()
        )
        print(account_id)
        assert account_id is not None

        # test getting by username
        account = get_account_by_username(account_username)
        assert account.id == account_id
        assert account.username == account_username

        # test getting by id
        account = get_account_by_id(account_id)
        assert account.id == account_id
        assert account.username == account_username

        # test deleting by id
        assert delete_account_by_id(account_id)

