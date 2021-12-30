import { useState } from 'react';

function PageProfile() {
  const [profileList] = useState([
    {
      uniqueId: 'bts-jin',
      name: '진',
      role: '서브보컬',
      mbti: 'INFP',
      instagramUrl: 'https://instagram.com/jin',
      profileImageUrl:
        'https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg',
    },
  ]);
  return (
    <div>
      <h2>PageProfile</h2>
      {profileList.length === 0 && '등록된 프로필이 없습니다.'}
      {profileList.map((profile) => {
        return (
          <div key={profile.uniqueId}>
            <img src={profile.profileImageUrl} />
            <h3>{profile.name}</h3>
            <ul>
              <li>{profile.name}</li>
              <li>{profile.role}</li>
              <li>{profile.instagramUrl}</li>
            </ul>
          </div>
        );
      })}
    </div>
  );
}

export default PageProfile;
