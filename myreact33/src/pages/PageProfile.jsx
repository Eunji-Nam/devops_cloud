import { useState } from 'react';

function PageProfile() {
  const [profileList] = useState({
    uniqueId: 'bts-jin',
    name: '진',
    role: '서브보컬',
    mbti: 'INFP',
    instagramUrl: 'https://instagram.com/jin',
    profileImageUrl:
      'https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg',
  });
  return (
    <div>
      <h2>PageProfile</h2>
      <img src={profileList.profileImageUrl} />
      <h3>{profileList.name}</h3>
      <ul>
        <li>{profileList.role}</li>
        <li>{profileList.mbti}</li>
        <li>{profileList.instagramUrl}</li>
      </ul>
    </div>
  );
}

export default PageProfile;
