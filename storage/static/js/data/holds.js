
export const roles = {
  1: {
    name: "Start",
    color: "#00ff4e"
  },
  2: {
    name: "Middle",
    color: "blue"
  },
  3: {
    name: "Finish",
    color: "red"
  },
  4: {
    name: "Foot",
    color: "#f802fc"
  }
}

export const getRoleName = (role_id) => {
  return roles[role_id].name
}


export const getColor = (role_id) => {
  return roles[role_id].color
};


