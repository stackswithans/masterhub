export const isLoggedIn = () => {
    return (
        window.localStorage.getItem("access_token") &&
        window.localStorage.getItem("refresh_token")
    );
};

export const saveSessionData = (sessionData: object) => {
    for (let key in sessionData) {
        window.localStorage.setItem(key, `${sessionData[key]}`);
    }
};

export const logOut = () => {
    window.localStorage.clear();
};
