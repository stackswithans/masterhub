export const host = window.location.protocol + "//" + window.location.hostname;
export const clientHost = host + ":" + location.port + "/";
export const apiHost = host + ":" + "8000" + "/";

//endpoints
const endpoints = {
    users: apiHost + "api/users/",
    call: apiHost + "call/",
    callSocket: `ws://${window.location.hostname + ":" + "8000"}/ws/call`,
};
export const postData = async (url = "", data = {}) => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    });
    return response.json();
};

export const postFormData = async (url = "", data: FormData) => {
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            Accept: "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: data,
    });
    return response.json();
};

export const getData = async (url = "") => {
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    });
    return response;
};

export const reverse = (path: string, pathParams?: Array<string>): string => {
    if (!(path in endpoints)) throw new Error("Invalid endpoint path name");
    if (!pathParams) pathParams = [];
    return [endpoints[path], ...pathParams].reduce(
        (accumulator, current) => accumulator + current
    );
};
