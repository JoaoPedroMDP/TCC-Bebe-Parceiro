import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectCampaignComponent } from './inspect-campaign.component';

describe('InspectCampaignComponent', () => {
  let component: InspectCampaignComponent;
  let fixture: ComponentFixture<InspectCampaignComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectCampaignComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectCampaignComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
