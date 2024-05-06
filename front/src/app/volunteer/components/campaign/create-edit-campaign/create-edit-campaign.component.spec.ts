import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEditCampaignComponent } from './create-edit-campaign.component';

describe('CreateEditCampaignComponent', () => {
  let component: CreateEditCampaignComponent;
  let fixture: ComponentFixture<CreateEditCampaignComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateEditCampaignComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateEditCampaignComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
