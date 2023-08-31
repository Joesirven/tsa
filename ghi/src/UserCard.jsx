import { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

const UserCard = () => {
    const [userData, setUserData] = useState({});
    const { fetchWithToken } = useToken();

    const fetchUserData = async() => {
        const url = "https://api.github.com/users"
        const data = await fetchWithToken(url)
        setUserData(data);
    }

    useEffect(() => {
        fetchUserData();
    }, [])

    return ( userData && <div>Data Recieved</div>)
}

export default UserCard
