import {useEffect, useState} from "react"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";


function JournalDetail() {
    const {token} = useAuthContext()
    const [isLoading, setIsLoading] = useState(true)
    const [journals, setJournal] = useState([]);

    const getUserIdFromToken = (token) => {
        const tokenParts = token.split(".");
        if (tokenParts.length === 3) {
            const payload = JSON.parse(atob(tokenParts[1]));
            const user_id = payload.account.id;
            return user_id;
        }
        return null;
        };

    const getData = async () => {
        setIsLoading(true)
        const user_id = getUserIdFromToken(token)
        try {
            const journalUrl = `http://localhost:8000/journal/${journal_id}`;
            const response = await fetch(journalUrl, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (response.ok) {
                const data = await response.json()
                setJournal(data)
            } else {
                console.error("Request error:", response.status)
            }
        } catch (e) {
            console.error("An error occured with request:", e)
        } finally {
            setIsLoading(false)
        }
    }
    useEffect(() => {
        if (token) {
            getData();
        }
    }, [token, journals.id]);

        return (
            <div>
                <h1>Journal Details</h1>

                <table className="table table-striped">
                <thead>
                    <tr>
                    <th>Location</th>
                    <th>Picture URL</th>
                    <th>Description</th>
                    <th>Rating</th>
                    <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {journals.map(journal => {
                    return (
                    <tr key={journal.id}>
                        <td>{journal.location}</td>
                        <td>{journal.picture_url}</td>
                        <td>{journal.description}</td>
                        <td>{journal.rating}</td>
                        <td>{journal.date}</td>
                    </tr>
                    );
                })}
                </tbody>
                </table>
                <div>
                    <button>Edit</button>
                </div>                   
            </div>
        );
    }
    export default JournalDetail;