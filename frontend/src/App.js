import "./App.css";
import {
  Button,
  ListItem as Item,
  Grid,
  InputBase,
  CircularProgress,
  Stack,
  Divider,
  ToggleButtonGroup,
  ToggleButton,
} from "@mui/material";
import { useRef, useState } from "react";
import getProfile from "./api/Profile";
import DownloadLink from "react-download-link";

function StyledDivider() {
  return (
    <Divider
      orientation='vertical'
      maxHeight
      style={{
        backgroundColor: "white",
        marginLeft: "10px",
        marginRight: "10px",
        height: "20px",
      }}
      variant={"fullWidth"}
    />
  );
}

function App() {
  const profileInput = useRef(null);
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);
  const [method, setMethod] = useState("scrape");
  const handler = () => {
    setLoading(true);
    getProfile(profileInput.current.value, method)
      .then((res) => {
        setProfile(res.data);
        setError(false);
        setLoading(false);
      })
      .catch((e) => {
        console.log(e);
        setProfile("That through an error");
        setLoading(false);
        setError(true);
      });
  };
  return (
    <div className='App'>
      <header className='App-header'>
        <div className='title'>LinkedIn Profile Scraper</div>
        <Grid container spacing={1} style={{ width: "80%" }}>
          <Grid item xs={2} alignSelf={"center"} value={method}>
            <ToggleButtonGroup
              value={method}
              sx={{
                backgroundColor: "#8e87e6",
                borderRadius: "20px",
              }}
              exclusive
              onChange={(e, v) => {
                if (v !== null) setMethod(v);
              }}
            >
              <ToggleButton
                value='scrape'
                sx={{
                  color: "#524827",
                  borderRadius: "20px",
                  "&.Mui-selected": {
                    backgroundColor: "#7c74e8",
                    color: "white",
                  },
                }}
              >
                Scraper
              </ToggleButton>
              <ToggleButton
                value='api'
                sx={{
                  color: "#524827",
                  borderRadius: "20px",
                  "&.Mui-selected": {
                    backgroundColor: "#7c74e8",
                    color: "white",
                  },
                }}
              >
                API
              </ToggleButton>
            </ToggleButtonGroup>
          </Grid>
          <Grid item xs={8}>
            <Item>
              <InputBase
                className='ProfileInput'
                placeholder='Type Profile URL to be scraped'
                inputRef={(r) => {
                  profileInput.current = r;
                }}
                onKeyDown={(event) => {
                  if (event.key === "Enter" && !loading) {
                    handler();
                  }
                }}
              />
            </Item>
          </Grid>
          <Grid item xs={2}>
            <Item>
              <Button
                variant='contained'
                style={{
                  borderRadius: "20px",
                  paddingLeft: "15px",
                  paddingRight: "15px",
                  paddingTop: "11px",
                  paddingBottom: "11px",
                }}
                onClick={handler}
                disabled={loading}
              >
                Scrape
              </Button>
            </Item>
          </Grid>
        </Grid>
        <Profile profile={profile} loading={loading} error={error} />
      </header>
    </div>
  );
}
function Profile({ profile = null, loading = false, error = false }) {
  console.log(profile);
  return loading ? (
    <CircularProgress />
  ) : error ? (
    <div>That threw an error!</div>
  ) : profile ? (
    <>
      <Stack
        style={{
          maxWidth: "80%",
          textAlign: "left",
          justifyContent: "flex-start",
        }}
      >
        <Item className='profileItem'>
          <b>Name</b>
          <StyledDivider />
          {profile.name}
        </Item>
        <Item className='profileItem'>
          <b>Title Description</b>
          <StyledDivider />
          {profile.titleDescription}
        </Item>
        <Item className='profileItem'>
          <b>Location</b>
          <StyledDivider />
          {profile.location}
        </Item>
        <Item className='profileItem'>
          <b>About</b>
          <StyledDivider />
          <span>{profile.about}</span>
        </Item>
        <Item className='profileItem'>
          <b>Experiences</b>
          <StyledDivider />
          <Stack style={{ maxHeight: "400px", overflow: "scroll" }}>
            {profile.experiences.map((item) => (
              <ul style={{}}>
                <li>Position: {item.position}</li>
                <li>Company: {item.company}</li>
                <li>Date Range: {item.dateRange}</li>
                <li>Location: {item.location}</li>
                {item?.type && <li>Job Type: {item.type}</li>}
                <li>Description: {item.description}</li>
              </ul>
            ))}
          </Stack>
        </Item>
        <Item className='profileItem'>
          <b>Education</b>
          <StyledDivider />
          <Stack style={{ maxHeight: "400px", overflow: "scroll" }}>
            {profile.education.map((item) => (
              <ul>
                <li>School: {item.name}</li>
                <li>Degree: {item.degree}</li>
                <li>Date Range: {item.dateRange}</li>
                <li>Description: {item.description}</li>
              </ul>
            ))}
          </Stack>
        </Item>
        <Item className='profileItem'>
          <b>Recommendations</b>
          <StyledDivider />
          <Stack style={{ maxHeight: "400px", overflow: "scroll" }}>
            {profile?.recommendations ??
              [].map((item) => (
                <ul>
                  <li>Recommender: {item.name}</li>
                  {item.profile !== "N/A" ? (
                    <li>
                      Profile: <a href={item.profile}>{item.profile}</a>
                    </li>
                  ) : (
                    <li>Profile: {item.profile}</li>
                  )}
                  <li>Date of Testimonial: {item.date}</li>
                  <li>Relationship: {item.relationship}</li>
                  <li>Testimonial: {item.testimonial}</li>
                </ul>
              ))}
          </Stack>
        </Item>
      </Stack>
      <DownloadLink
        label='Save'
        style={{
          color: "white",
          fontSize: "20px",
          margin: "20px",
          marginTop: "10px",
        }}
        filename='scraped_profile.json'
        exportFile={() => JSON.stringify(profile)}
      />
    </>
  ) : (
    <></>
  );
}

export default App;
