import { useState, useEffect } from "react"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react"
import { useNavigate } from "react-router-dom"


function JournalCreate() {
    const { token } = useAuthContext()
    const navigate = useNavigate()
    const [formData, setFormData] = useState({
        location: '',
        picture_url: '',
        description: '',
        rating: '',
        date: '',
        users_id: '',
    })
    const [isLoading, setIsLoading] = useState(false)
    const [isSubmitted, setIsSubmitted] = useState(false)

    const handleSubmit = async (e) => {
        e.preventDefault()
        setIsLoading(true);
        const journalUrl = "http://localhost:8000/journal/create"

        if (!formData.location || !formData.description || !formData.date || !formData.rating) {
            setIsLoading(false)
            return
        }


        const fetchConfig = {
            method: 'POST',
            body: JSON.stringify(formData),
            headers: {
                "Content-Type": 'application/json',
                Authorization: `Bearer ${token}`,
            },
        }

        try {
            const response = await fetch(journalUrl, fetchConfig)
            if (!response.ok) {
                const errorMessage = await response.text()
            } else {
                setIsSubmitted(true)
                setFormData({
                    location: "",
                    picture_url: "",
                    description: "",
                    rating: "",
                    date: "",
                });
                navigate("/journal")
            }
        } catch(e){

        } finally {
            setIsLoading(false)
        }
    }
    const getUserIdFromToken = (token) => {
        const tokenParts = token.split(".");
        if (tokenParts.length === 3) {
        const payload = JSON.parse(atob(tokenParts[1]));
        const user_id = payload.account.id;
        return user_id;
        }

        return null;
    };


    useEffect(() => {
        if (token) {
            try {
                const user_id = getUserIdFromToken(token)
                if (user_id) {
                    setFormData((prevData) => ({
                    ...prevData,
                    users_id: user_id,
                    }));
                }       
            } catch (e) {
            }
        }
    }, [token]);
    
    const handleFormChange = (e) => {
        const value = e.target.value
        const inputJournal = e.target.name
        setFormData({
            ...formData,
            [inputJournal]: value
        })
    }
    
    return (
        <div className="row">
            {isSubmitted && <Redirect to="/journal" />}
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create a new journal entry</h1>
                        <form onSubmit={handleSubmit} id="create-journal-form">           
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.location} placeholder="Enter Location" required type="text" name="location" id="location" className="form-control" />
                            <label htmlFor="location">Location</label>
                        </div>          
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.picture_url} placeholder="Enter picture url" required type="text" name="picture_url" id="picture_url" className="form-control" />
                            <label htmlFor="picture_url">Picture Url</label>
                        </div>           
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.description} placeholder="Enter description" required type="text" name="description" id="description" className="form-control" />
                            <label htmlFor="description">Description</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.rating} placeholder="Enter rating" required type="text" name="rating" id="rating" className="form-control" />
                            <label htmlFor="rating">Rating</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={handleFormChange} value={formData.date} placeholder="Enter date" required type="date" name="date" id="date" className="form-control" />
                            <label htmlFor="date">Date</label>
                        </div>
                        <button className="btn btn-primary" disabled={isLoading}>
                            {isLoading ? "Creating ..." : "Create New Journal"} 
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}
export default JournalCreate