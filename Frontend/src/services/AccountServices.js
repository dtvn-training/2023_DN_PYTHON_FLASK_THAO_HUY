import axios from "axios";
import api from "../api/axios";

class AccountServices {
    //Call request API login by method POST
    getAllAccount() {
        return api.get('/all_user');
    }

    postNewAccount(data) {
        return api.post('/new_user', data);
    }

    searchAccount(data) {
        return api.post('/user_info',data);
    }

    updateAccount(data) {
        return api.put('/update_user', data);
    }

    deleteAccount(data) {
      return api.delete('/delete_user', data);
    }

    deleteAllAccount(data) {
      return api.delete('/delete_all_user', data);
    }
}

export default new AccountServices();

