import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectVolunteerComponent } from './inspect-volunteer.component';

describe('InspectVolunteerComponent', () => {
  let component: InspectVolunteerComponent;
  let fixture: ComponentFixture<InspectVolunteerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectVolunteerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectVolunteerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
