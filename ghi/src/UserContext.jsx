import React, { createContext, useContext } from "react";

// Create a UserContext
const UserContext = createContext();

export function useUserContext() {
  return useContext(UserContext);
}

// Create a UserProvider (usually in a separate file)
export function UserProvider({ children }) {
  // Your user data and logic here...
  const userId = /* Fetch or get the user ID from your authentication */

  return (
    <UserContext.Provider value={{ userId }}>
      {children}
    </UserContext.Provider>
  );
}